# main.py
from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from app.qa_engine import run_qa_checks

app = FastAPI()

@app.post("/upload_and_check")
async def upload_and_check(
    drawing_id: str = Form(...),
    revision: str = Form(...),
    drawing_title: str = Form(...),
    formats_received: str = Form(...),
    discipline: str = Form(...),
    drawing_type: str = Form(...),
    drawing_status: str = Form(...),
    notes: Optional[str] = Form(None),
    dxf_file: UploadFile = File(...),
    pdf_file: UploadFile = File(...)
):
    # Read uploaded files
    dxf_content = await dxf_file.read()
    pdf_content = await pdf_file.read() if pdf_file else None

    # Run QA checks using provided DXF/PDF contents and metadata
    result = run_qa_checks({
        "drawing_id": drawing_id,
        "revision": revision,
        "drawing_title": drawing_title,
        "formats_received": formats_received,
        "discipline": discipline,
        "drawing_type": drawing_type,
        "drawing_status": drawing_status,
        "notes": notes or "",
        "dxf_bytes": dxf_content,
        "pdf_bytes": pdf_content
    })

    # Return JSON with summary, results, and Markdown report
    return {
        "summary": result["summary"],
        "results": result["results"],
        "report_markdown": result["report_markdown"]
    }
@app.get("/")
def read_root():
    return {"message": "Hello, this is the Drawing QA Checker. Use POST /upload_and_check to run checks."}
