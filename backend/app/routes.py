from flask import request, jsonify
from app import app
from app.services.prompt_generation import generate_prompt
# from app.services.evaluation_data_generation import generate_test_cases
# from app.services.prompt_testing import test_prompts, elo_rating_system

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt_api():
    topic = request.json.get('topic')
    prompt = generate_prompt(topic)
    print({'prompt': prompt})

    # return jsonify({'prompt': prompt})

