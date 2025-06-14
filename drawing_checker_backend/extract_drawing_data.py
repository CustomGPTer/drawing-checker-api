import ezdxf
import pdfplumber

def parse_dxf(file_path):
    doc = ezdxf.readfile(file_path)
    modelspace = doc.modelspace()
    entities = []
    for e in modelspace:
        if e.dxftype() in ['LWPOLYLINE', 'TEXT', 'INSERT']:
            entities.append({
                'type': e.dxftype(),
                'layer': e.dxf.layer,
                'handle': e.dxf.handle
            })
    return entities

def parse_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        first_page = pdf.pages[0]
        return first_page.extract_text()
