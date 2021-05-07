FROM python:3.9

ADD src/requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY src /sb_api_2
WORKDIR /sb_api_2

ENTRYPOINT ["python"]
CMD ["sb_worker.py"]
