FROM python:3.6.5-alpine3.7

ENV HOME=/usr/src/app
WORKDIR $HOME

COPY . $HOME

RUN apk --no-cache add build-base
RUN pip install -r requirements.txt

EXPOSE 6543
CMD python app.py
