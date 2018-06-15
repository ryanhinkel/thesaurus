FROM python:3.6.5-slim

ENV HOME=/usr/src/app
WORKDIR $HOME

COPY . $HOME

RUN apt-get update && apt-get -y install build-essential && rm -Rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

EXPOSE 6543
CMD python app.py
