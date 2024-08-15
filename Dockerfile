FROM python:3.10-slim

WORKDIR /backend

COPY . /backend

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

EXPOSE 80

ENV NAME LLM_Prompt_Engine

CMD ["python", "app.py"]
