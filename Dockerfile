FROM python:3.6.5-slim

ENV HOME=/usr/src/app
WORKDIR $HOME

COPY requirements.txt $HOME

RUN apt-get update && \
  apt-get -y install build-essential && \
  rm -Rf /var/lib/apt/lists/* && \
  pip install --no-cache-dir -r requirements.txt && \
  apt-get -y purge build-essential

COPY . $HOME

EXPOSE 6543
CMD gunicorn thesaurus.wsgi:application -b 0.0.0.0:6543
