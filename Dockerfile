FROM python:3.7-alpine

RUN adduser -D heartbyte
WORKDIR /home/heartbyte
COPY . app

RUN pip install -r app/requirements.txt
RUN chmod +x app/start.sh

ENV FLASK_APP app/application.py

RUN chown -R heartbyte:heartbyte ./
USER heartbyte
EXPOSE 5001

ENTRYPOINT ["app/start.sh"]