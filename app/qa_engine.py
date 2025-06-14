from qa_checks import qa_checks
import ezdxf
import io
import pdfplumber


def run_qa_checks(data: dict):
    dxf_bytes = data.get("dxf_bytes")
    pdf_bytes = data.get("pdf_bytes")
    results = []

    def add_result(check_key, result, explanation):
        base = {
            "question": len(results) + 1,
            "check": qa_checks.get(check_key, {}).get("description", check_key),
            "result": result,
            "explanation": explanation
        }

        if result in ["❌ FAIL", "⚠️ FLAG"] and check_key in qa_checks:
            d = qa_checks[check_key].get("diagnostic", {})
            base["deep_dive"] = {
                "likely_cause": d.get("likely_cause"),
                "risk": d.get("risk"),
                "fix": d.get("fix", []),
                "CESWI": qa_checks[check_key].get("CESWI"),
                "UUCESWI": qa_checks[check_key].get("UUCESWI"),
                "BestPractice": qa_checks[check_key].get("BestPractice")
            }

        results.append(base)

    if not dxf_bytes:
        add_result("pipe_layout", "❌ FAIL", "No DXF file provided")
        return {
            "summary": "No DXF provided.",
            "results": results,
            "report_markdown": "❌ FAIL – No DXF file found."
        }

    # --- DXF Parsing ---
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

    # Example checks
    if any(e["type"] == "LWPOLYLINE" for e in entities):
        add_result("pipe_layout", "✅ PASS", "Polylines found for pipe layout")
    else:
        add_result("pipe_layout", "❌ FAIL", "No polylines (pipe runs) detected in DXF")

    if any("INV" in e["layer"].upper() for e in entities):
        add_result("invert_levels", "✅ PASS", "Layer names suggest invert levels")
    else:
        add_result("invert_levels", "⚠️ FLAG", "No layers clearly named for invert or level")

    # --- PDF Parsing ---
    if pdf_bytes:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            text = pdf.pages[0].extract_text() or ""

            if "FOR CONSTRUCTION" in text.upper():
                add_result("drawing_status", "✅ PASS", "PDF marked For Construction")
            elif "FOR INFORMATION" in text.upper():
                add_result("drawing_status", "⚠️ FLAG", "PDF marked For Information")
            elif "TENDER" in text.upper():
                add_result("drawing_status", "⚠️ FLAG", "PDF marked for Tender")
            else:
                add_result("drawing_status", "❌ FAIL", "No clear drawing status found in PDF")
    else:
        add_result("drawing_status", "⚠️ FLAG", "No PDF file uploaded — status unknown")

    # --- Markdown Output ---
    md = f"# QA Report – {data.get('drawing_id', 'N/A')}\n\n"
    md += f"**Revision:** {data.get('revision', 'Unknown')}\n\n"
    md += "| No. | Result | Check | Explanation |\n|-----|--------|--------|-------------|\n"

    for r in results:
        md += f"| {r['question']} | {r['result']} | {r['check']} | {r['explanation']} |\n"
        if "deep_dive" in r:
            d = r["deep_dive"]
            md += f"\n> 📉 **Likely Cause:** {d['likely_cause']}\n"
            md += f"> 🚨 **Risk if Ignored:** {d['risk']}\n"
            md += f"> 📘 **Guidance:**\n"
            md += f"> - CESWI: {d['CESWI']}\n"
            md += f"> - UUCESWI: {d['UUCESWI']}\n"
            md += f"> - Best Practice: {d['BestPractice']}\n"
            md += f"> 🛠 **Fix Options:**\n"
            for fix in d["fix"]:
                md += f"> - {fix}\n"

    # Summary at the bottom
    counts = {
        "✅ PASS": sum(1 for r in results if r["result"] == "✅ PASS"),
        "⚠️ FLAG": sum(1 for r in results if r["result"] == "⚠️ FLAG"),
        "❌ FAIL": sum(1 for r in results if r["result"] == "❌ FAIL"),
    }

    md += "\n---\n\n## ✅ QA Summary\n"
    for key, val in counts.items():
        md += f"- {key}: {val}\n"

    flagged = [r for r in results if r["result"] in ["❌ FAIL", "⚠️ FLAG"]]
    if flagged:
        md += "\n## 🧾 Final Verdict:\nDrawing **requires revision** due to:\n"
        for r in flagged:
            md += f"- {r['check']}: {r['explanation']}\n"
    else:
        md += "\n## 🧾 Final Verdict:\nDrawing is **buildable with no comments**."

    return {
        "summary": f"QA check complete for {data.get('drawing_id', 'N/A')}",
        "results": results,
        "report_markdown": md
    }


