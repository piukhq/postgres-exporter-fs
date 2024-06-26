FROM ghcr.io/binkhq/python:3.9

WORKDIR /app
ADD . .
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "main.py"]