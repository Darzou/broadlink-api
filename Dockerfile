FROM python:3.9.6-slim

LABEL maintainer="farirat"

EXPOSE 5000/tcp
VOLUME ["/var/log/broadlink"]

WORKDIR /app
ADD . /app

RUN pip install -r requirements.pip

CMD [ "python3", "-m" , "flask", "run"]
