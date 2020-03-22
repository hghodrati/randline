FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
    libssl-dev \
    unzip \
    htop \
    jq \
    procps \
    screen \
    vim \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /usr/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV APPPATH="/usr/app"
ENV PYTHONPATH "${PYTHONPATH}:${APPPATH}"
