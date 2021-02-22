FROM python:alpine

RUN apt-get update -y
RUN apt-get install -y python-pip

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD [ "python main.py" ]
