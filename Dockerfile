FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales python3 python3-pip && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt