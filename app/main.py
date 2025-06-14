
from fastapi import FastAPI
from pydantic import BaseModel
from app.qa_engine import run_qa_checks

app = FastAPI()

class QARequest(BaseModel):
    drawing_id: str
    revision: str
    drawing_title: str
    formats_received: str
    discipline: str
    drawing_type: str
    drawing_status: str
    notes: str = ""

@app.post("/qa_check")
def qa_check(data: QARequest):
    result = run_qa_checks(data.dict())
    return {"summary": f"QA check completed for {data.drawing_id}", "results": result}
from fastapi import UploadFile, File, Form

@app.post("/upload_and_check")
async def upload_and_check(
    drawing_id: str = Form(...),
    revision: str = Form(...),
    drawing_title: str = Form(...),
    formats_received: str = Form(...),
    discipline: str = Form(...),
    drawing_type: str = Form(...),
    drawing_status: str = Form(...),
    notes: str = Form(""),
    dxf_file: UploadFile = File(...),
    pdf_file: UploadFile = File(None)
):
    dxf_content = await dxf_file.read()
    pdf_content = await pdf_file.read() if pdf_file else None

    result = run_qa_checks({
        "drawing_id": drawing_id,
        "revision": revision,
        "drawing_title": drawing_title,
        "formats_received": formats_received,
        "discipline": discipline,
        "drawing_type": drawing_type,
        "drawing_status": drawing_status,
        "notes": notes,
        "dxf_bytes": dxf_content,
        "pdf_bytes": pdf_content
    })

    return {"summary": f"QA check complete for {drawing_id}", "results": result}
