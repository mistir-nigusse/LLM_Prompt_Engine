from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from utils.pdf_utils import MyPDF
from utils.text_splitter_utils import MyTextSplitter
from utils.vector_store_utils import MyVectorStore
from utils.langchain import MyLangChain

app = Flask(__name__)
CORS(app)

@app.route('/get_prompts', methods=['POST'])
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

    langchain = MyLangChain()
    conversation_chain = langchain.generate_prompts_chain(base_retriever=retriever)

    result = conversation_chain.invoke({
        "user_prompt": prompt,
        "num_of_prompts_to_generate": 5,
    })

    response_content = result['response'].content

    if isinstance(response_content, str):
        response_content = response_content.strip()
        try:
            prompts_generated = json.loads(response_content)
        except json.JSONDecodeError as e:
            return jsonify({'error': 'Invalid JSON response', 'details': str(e)}), 500


        return jsonify({'prompts': prompts_generated})
    else:
        return jsonify({'error': 'Invalid response format'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5003)
