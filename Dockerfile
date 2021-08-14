FROM python:3.6.11-slim-buster

WORKDIR /usr/src/app
ARG ENVSHORTNER
ENV ENVSHORTNER=$ENVSHORTNER
COPY requirements.txt ./


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "gunicorn", "-w", "5", "-b", "0.0.0.0:8000", "--timeout", "300", "server:api" ]
