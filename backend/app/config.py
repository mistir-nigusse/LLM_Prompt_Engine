import os
from dotenv import load_dotenv


class Config:
    def load():
        load_dotenv()
        return {
        "OPENAI_API_KEY"  : os.environ.get('OPENAI_API_KEY')

        }
