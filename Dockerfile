FROM python:3.7-alpine
RUN apk update
RUN apk add --no-cache make build-base
RUN apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "application.py"]