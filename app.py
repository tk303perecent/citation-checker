from flask import Flask, request, jsonify
from eyecite import get_citations

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    text = request.json.get("text", "")
    citations = get_citations(text)
    return jsonify({"citations": [str(c) for c in citations]})

if __name__ == '__main__':
    app.run(debug=True)
