
FROM python:3.7-alpine

RUN apk update && apk add dos2unix
RUN adduser -D heartbyte
WORKDIR /home/heartbyte

COPY . app
RUN pip install -r app/requirements.txt
#For Windows host only
#RUN  dos2unix app/scripts/startup.sh
#For Linux host only
RUN  chmod +x app/scripts/startup.sh

ENV FLASK_APP app/application.py
RUN chown -R heartbyte:heartbyte ./
USER heartbyte
EXPOSE 5001

ENTRYPOINT ["app/scripts/startup.sh"]

