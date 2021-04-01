FROM ubuntu:latest

RUN apt-get update -y &&\
    apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install petname==2.6

ENTRYPOINT ["python"]
CMD ["app.py"]
