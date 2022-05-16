FROM python:3.10.4-slim

WORKDIR /app
COPY . /app

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python3", "update.py"]