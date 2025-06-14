import ezdxf
import io
import pdfplumber


def run_qa_checks(data: dict):
    dxf_bytes = data.get("dxf_bytes")
    pdf_bytes = data.get("pdf_bytes")
    results = []

    if not dxf_bytes:
        return [{"question": 0, "result": "❌ FAIL", "explanation": "No DXF file provided"}]

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

    if any(e["type"] == "LWPOLYLINE" for e in entities):
        results.append({"question": 1, "result": "✅ PASS", "explanation": "Polylines found for pipe layout"})
    else:
        results.append({"question": 1, "result": "❌ FAIL", "explanation": "No polylines (pipe runs) detected in DXF"})

    if any("INV" in e["layer"].upper() for e in entities):
        results.append({"question": 2, "result": "✅ PASS", "explanation": "Layer names suggest invert levels"})
    else:
        results.append({"question": 2, "result": "⚠️ FLAG", "explanation": "No layers clearly named for invert or level"})

    # --- PDF Parsing ---
    if pdf_bytes:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            text = pdf.pages[0].extract_text() or ""

            if "FOR CONSTRUCTION" in text.upper():
                results.append({"question": 3, "result": "✅ PASS", "explanation": "PDF marked For Construction"})
            elif "FOR INFORMATION" in text.upper():
                results.append({"question": 3, "result": "⚠️ FLAG", "explanation": "PDF marked For Information"})
            elif "TENDER" in text.upper():
                results.append({"question": 3, "result": "⚠️ FLAG", "explanation": "PDF marked for Tender"})
            else:
                results.append({"question": 3, "result": "❌ FAIL", "explanation": "No clear drawing status found in PDF"})
    else:
        results.append({"question": 3, "result": "⚠️ FLAG", "explanation": "No PDF file uploaded — status unknown"})

    return results

