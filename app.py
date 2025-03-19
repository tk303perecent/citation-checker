from flask import Flask, request, jsonify
from eyecite import get_citations
import pdfplumber
import docx
import os

app = Flask(__name__)

# Route for text input
@app.route('/extract', methods=['POST'])
def extract():
    data = request.json
    text = data.get("text", "")
    citations = get_citations(text)
    return jsonify({"citations": [str(c) for c in citations]})

# Route for file uploads
@app.route('/extract/upload', methods=['POST'])
def extract_from_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    filename = file.filename

    # Extract text from file
    text = ""
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file)
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    # Process extracted text
    citations = get_citations(text)
    return jsonify({"citations": [str(c) for c in citations]})

# Extract text from PDFs
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Extract text from DOCX files
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

if __name__ == '__main__':
    app.run(debug=True)
