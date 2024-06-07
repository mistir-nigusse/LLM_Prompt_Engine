from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get_prompt', methods=['POST'])
def generate_prompt():
    pdf = request.files['pdf']
    prompt = request.form['prompt']

    generated_prompts = [
        f"Generated prompt 1 for: {prompt}",
        f"Generated prompt 2 for: {prompt}",
        f"Generated prompt 3 for: {prompt}"
    ]

    return jsonify({'prompts': generated_prompts})


if __name__ == '__main__':
   app.run(host='localhost', port=5000)


