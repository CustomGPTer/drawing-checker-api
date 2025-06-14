from extract_drawing_data import parse_dxf, parse_pdf
from utils import is_similar_filename
from qa_scoring import calculate_score

# Replace these with your actual file paths when running locally
dxf_entities = parse_dxf("example.dxf")
pdf_text = parse_pdf("example.pdf")

print("DXF Entities:", dxf_entities[:5])
print("PDF Text Snippet:", pdf_text[:300])

filename1 = "DR-MECH-001.pdf"
filename2 = "DR_MECH_001.dxf"
print("Filenames match?", is_similar_filename(filename1, filename2))

qa_results = [
    {"question": 1, "result": "PASS"},
    {"question": 2, "result": "FAIL"},
    {"question": 3, "result": "FLAG"}
]
print("Compliance Score:", calculate_score(qa_results))
