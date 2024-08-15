.PHONY: install test docker-build docker-run clean

install:
    poetry install

test:
    poetry run pytest

docker-build:
    docker build -t llm_prompt_engine .

docker-run:
    docker run -p 80:80 llm_prompt_engine

clean:
    rm -rf __pycache__
