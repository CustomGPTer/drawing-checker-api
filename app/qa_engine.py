from .qa_checks import qa_checks
import ezdxf
import io
import pdfplumber
import json

def run_qa_checks(data: dict):
    # Extract raw files
    dxf_bytes = data.get("dxf_bytes")
    pdf_bytes = data.get("pdf_bytes")

    # 🔧 Helper: fallback-safe metadata parser
    def safe_field(key, fallback):
        val = data.get(key)
        if val is None:
            return fallback
        if isinstance(val, str):
            return val.strip()
        return str(val).strip()

    # ✅ Parse metadata safely – allows Custom GPTs to skip some fields
    discipline = safe_field("discipline", "combined").lower()
    drawing_id = safe_field("drawing_id", "Unknown")
    revision = safe_field("revision", "Unknown")
    drawing_title = safe_field("drawing_title", "Untitled")
    formats_received = safe_field("formats_received", "Unknown")
    drawing_type = safe_field("drawing_type", "Unspecified")
    drawing_status = safe_field("drawing_status", "Unspecified")
    notes = safe_field("notes", "")

    results = []

    # Load standards file (CESWI/UUCESWI/etc)
    with open("standards.json", encoding="utf-8") as f:
        standards = json.load(f)

    # Helper function to filter checks by discipline/category
    def check_applicable(category):
        if discipline == "combined":
            return True
        return category.lower() == discipline

    # Append result to report list with optional diagnostic deep dive
    def add_result(check_key, result, explanation):
        check = qa_checks.get(check_key, {})
        category = check.get("category", "").lower()
        if not check_applicable(category) and result != "N/A":
            return
        base = {
            "question": len(results) + 1,
            "check": check.get("description", check_key),
            "result": result,
            "explanation": explanation
        }
        if result in ["FAIL", "FLAG"] and check_key in qa_checks:
            d = check.get("diagnostic", {})
            base["deep_dive"] = {
                "likely_cause": d.get("likely_cause"),
                "risk": d.get("risk"),
                "fix": d.get("fix", []),
                "CESWI": check.get("CESWI"),
                "UUCESWI": check.get("UUCESWI"),
                "BestPractice": check.get("BestPractice")
            }
        results.append(base)

    if not dxf_bytes:
        add_result("pipe_layout", "FAIL", "No DXF file provided")
        return {
            "summary": "No DXF provided.",
            "results": results,
            "report_markdown": "FAIL – No DXF file found."
        }

    dxf_stream = io.BytesIO(dxf_bytes)
    doc = ezdxf.read(dxf_stream)
    modelspace = doc.modelspace()

    entities = []
    for e in modelspace:
        if e.dxftype() in ["TEXT", "MTEXT", "LWPOLYLINE", "LINE", "INSERT"]:
            entities.append({
                "type": e.dxftype(),
                "layer": e.dxf.layer,
                "handle": e.dxf.handle
            })

    if any(e["type"] == "LWPOLYLINE" for e in entities):
        add_result("pipe_layout", "PASS", "Polylines found for pipe layout")
    else:
        add_result("pipe_layout", "FAIL", "No polylines (pipe runs) detected in DXF")

    if any("INV" in e["layer"].upper() for e in entities):
        add_result("invert_levels", "PASS", "Layer names suggest invert levels")
    else:
        add_result("invert_levels", "FLAG", "No layers clearly named for invert or level")

    if pdf_bytes:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            text = pdf.pages[0].extract_text() or ""
            if "FOR CONSTRUCTION" in text.upper():
                add_result("drawing_status", "PASS", "PDF marked For Construction")
            elif "FOR INFORMATION" in text.upper():
                add_result("drawing_status", "FLAG", "PDF marked For Information")
            elif "TENDER" in text.upper():
                add_result("drawing_status", "FLAG", "PDF marked for Tender")
            else:
                add_result("drawing_status", "FAIL", "No clear drawing status found in PDF")
    else:
        add_result("drawing_status", "FLAG", "No PDF file uploaded — status unknown")

    for key, check in qa_checks.items():
        if key in ["pipe_layout", "invert_levels", "drawing_status"]:
            continue
        if not check_applicable(check.get("category", "")):
            add_result(key, "N/A", "Not applicable to this drawing type.")
        else:
            if key == "penetrations" and "penetration_required" in standards:
                add_result(key, "FLAG", f"Penetration sleeves required – {standards['penetration_required']['standard']}")
            elif key == "pipe_layout" and "pipe_clearance_min" in standards:
                add_result(key, "FLAG", f"Check pipe clearance ≥ {standards['pipe_clearance_min']['value']} {standards['pipe_clearance_min']['unit']}")
            else:
                add_result(key, "FLAG", "Check logic not implemented – flagged for manual review.")

    # ✅ BEGIN REPORT
    md = f"# QA Report – {drawing_id}\n\n"
    md += f"**Revision:** {revision}  \n"
    md += f"**Title:** {drawing_title}  \n"
    md += f"**Discipline (raw):** `{discipline}`  \n"
    md += f"**Drawing Type:** {drawing_type}  \n"
    md += f"**Status:** {drawing_status}  \n"
    md += f"**Formats Received:** {formats_received}  \n"
    if notes:
        md += f"**Notes:** {notes}  \n"

    unusual = []
    if discipline not in ["civils", "mechanical", "electrical", "combined"]:
        unusual.append(f"⚠️ Unrecognised discipline: `{discipline}`")
    if drawing_status.lower() not in ["for construction", "tender", "for information", "unknown"]:
        unusual.append(f"⚠️ Unusual drawing status: `{drawing_status}`")
    if formats_received.lower() not in ["pdf", "dxf", "both"]:
        unusual.append(f"⚠️ Unexpected formats value: `{formats_received}`")

    if unusual:
        md += "\n\n## ⚠️ Metadata Warnings\n"
        for u in unusual:
            md += f"- {u}\n"

    md += "\n\n| No. | Result | Check | Explanation |\n|-----|--------|--------|-------------|\n"
    for r in results:
        md += f"| {r['question']} | {r['result']} | {r['check']} | {r['explanation']} |\n"
        if "deep_dive" in r:
            d = r["deep_dive"]
            md += f"\n> Likely Cause: {d['likely_cause']}\n"
            md += f"> Risk if Ignored: {d['risk']}\n"
            md += f"> Guidance:\n"
            md += f"> - CESWI: {d['CESWI']}\n"
            md += f"> - UUCESWI: {d['UUCESWI']}\n"
            md += f"> - Best Practice: {d['BestPractice']}\n"
            md += f"> Fix Options:\n"
            for fix in d["fix"]:
                md += f"> - {fix}\n"

    counts = {
        "PASS": sum(1 for r in results if r["result"] == "PASS"),
        "FLAG": sum(1 for r in results if r["result"] == "FLAG"),
        "FAIL": sum(1 for r in results if r["result"] == "FAIL")
    }

    md += "\n---\n\n## QA Summary\n"
    for key, val in counts.items():
        md += f"- {key}: {val}\n"

    flagged = [r for r in results if r["result"] in ["FAIL", "FLAG"]]
    if flagged:
        md += "\n## Final Verdict:\nDrawing requires revision due to:\n"
        for r in flagged:
            md += f"- {r['check']}: {r['explanation']}\n"
    else:
        md += "\n## Final Verdict:\nDrawing is buildable with no comments."

    return {
        "summary": f"QA check complete for {drawing_id}",
        "results": results,
        "report_markdown": md
    }
