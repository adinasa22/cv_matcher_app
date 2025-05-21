import PyPDF2
import tempfile
import os
from docx import Document


def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        uploaded_file.seek(0)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        try:
            with open(tmp_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            return text
        except Exception as e:
            return f"Error reading PDF file: {e}"
        finally:
            os.remove(tmp_path)
    elif uploaded_file.name.endswith('.docx'):
        uploaded_file.seek(0)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        try:
            doc = Document(tmp_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            return f"Error reading DOCX file: {e}"
        finally:
            os.remove(tmp_path)
    else:
        return "Unsupported file format. Please upload a PDF or DOCX file."