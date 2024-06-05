from openai import OpenAI
from app.config import Config

config = Config.load()

client = OpenAI(api_key=config['OPENAI_API_KEY'])


def generate_prompt(topic):

  response = client.chat.completions.create(
      messages=[
          {
              "role": "system",
              "content": "You are a helpful assistant."
          },
          {
              "role": "user",
              "content": f"Generate a prompt about {topic}"
          }
      ],
      model="gpt-3.5-turbo"
  )

  # Extract the prompt text from the response
 
  prompt = response.choices[0].message.content.strip()
  print(prompt)
  return prompt


