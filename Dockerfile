FROM alpine:latest

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip --no-cache-dir install -r requirements.txt

CMD ["/opt/venv/bin/python3","app.py"]
