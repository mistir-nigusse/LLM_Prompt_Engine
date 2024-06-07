from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.pdf_utils import MyPDF
from utils.text_splitter_utils import MyTextSplitter
from utils.vector_store_utils import MyVectorStore

app = Flask(__name__)
CORS(app)

@app.route('/get_prompt', methods=['POST'])
def generate_prompt():
    pdf = request.files['pdf']
    prompt = request.form['prompt']

    pdf_processor = MyPDF(pdf)
    raw_text = pdf_processor.get_pdf_text()

    text_splitter = MyTextSplitter(raw_text)
    text_chunks = text_splitter.get_text_chunks()

    vector_store = MyVectorStore()
    chroma_vector_store = vector_store.embed_text_and_return_vectorstore(text_chunks)

    retriever = vector_store.get_retriever(chroma_vector_store)

    # placeholder response
    generated_prompts = [
        f"Generated prompt 1 for: {prompt}",
        f"Generated prompt 2 for: {prompt}",
        f"Generated prompt 3 for: {prompt}"
    ]

    return jsonify({'prompts': generated_prompts})

if __name__ == '__main__':
    app.run(debug=True)
