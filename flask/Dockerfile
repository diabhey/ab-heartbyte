FROM python:3.7-alpine

RUN apk update && \
    adduser -D heartbyte

WORKDIR /home/heartbyte
COPY . app
RUN chown -R heartbyte:heartbyte ./

RUN pip install -r app/requirements.txt
EXPOSE 80

ENTRYPOINT ["python3", "app/application.py"]