from app.qa_engine import run_qa_checks

mock_data = {
    "drawing_id": "DR-C-1001",
    "revision": "P02",
    "drawing_title": "Drainage Layout",
    "formats_received": "Both",
    "discipline": "Civils",
    "drawing_type": "General Arrangement",
    "drawing_status": "For Construction",
    "notes": "Test run without DXF/PDF",
    "dxf_bytes": b"",  # load actual bytes here for real run
    "pdf_bytes": b""   # load actual bytes here for real run
}

output = run_qa_checks(mock_data)
print(output["report_markdown"])
