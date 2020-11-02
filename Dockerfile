FROM python:3.7-alpine

ADD app.py /

CMD [ "python", "./app.py" ]

