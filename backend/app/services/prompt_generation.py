from openai import OpenAI
from app.config import Config

config = Config.load()
api_key = config['OPENAI_API_KEY']
client = OpenAI(api_key=api_key)
def generate_prompt(topic):

    response = client.chat.completions.create(
    messages=[
        {
          {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a prompt about {topic}"}
        }
    ],
    model="gpt-3.5-turbo",
)

    return response['choices'][0]['message']['content'].strip()
