
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
