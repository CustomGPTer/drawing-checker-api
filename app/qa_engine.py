import ezdxf
import io

def run_qa_checks(data: dict):
    dxf_bytes = data.get("dxf_bytes")

    if not dxf_bytes:
        return [{"question": 0, "result": "❌ FAIL", "explanation": "No DXF file provided"}]

    # Load DXF from bytes
    dxf_stream = io.BytesIO(dxf_bytes)
    doc = ezdxf.read(dxf_stream)
    modelspace = doc.modelspace()

    # Sample entity extraction (text and polylines)
    entities = []
    for e in modelspace:
        if e.dxftype() in ["TEXT", "MTEXT", "LWPOLYLINE", "LINE", "INSERT"]:
            entities.append({
                "type": e.dxftype(),
                "layer": e.dxf.layer,
                "handle": e.dxf.handle
            })

    # Sample QA result based on what we found
    results = []

    if any(e["type"] == "LWPOLYLINE" for e in entities):
        results.append({"question": 1, "result": "✅ PASS", "explanation": "Polylines found for pipe layout"})
    else:
        results.append({"question": 1, "result": "❌ FAIL", "explanation": "No polylines (pipe runs) detected in DXF"})

    if any("INV" in e["layer"].upper() for e in entities):
        results.append({"question": 2, "result": "✅ PASS", "explanation": "Layer names suggest invert levels"})
    else:
        results.append({"question": 2, "result": "⚠️ FLAG", "explanation": "No layers clearly named for invert or level"})

    return results
