import os
from pdfminer.high_level import extract_text
from docx import Document

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise Exception("Unsupported file format")
