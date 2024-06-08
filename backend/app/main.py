from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    pdf = request.files['pdf']
    prompt = request.form['prompt']

    # Here you would process the PDF and generate prompts based on the input
    # This is just a placeholder response
    generated_prompts = [
        f"Generated prompt 1 for: {prompt}",
        f"Generated prompt 2 for: {prompt}",
        f"Generated prompt 3 for: {prompt}"
    ]

    return jsonify({'prompts': generated_prompts})

if __name__ == '__main__':
    app.run(debug=True)
