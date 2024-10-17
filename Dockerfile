FROM python:3.11

WORKDIR /usr/app

RUN apt update

CMD [ "bash", "-c", "tail -f /dev/null" ]