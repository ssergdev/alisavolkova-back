FROM python:3.8-alpine 
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev zlib-dev libressl-dev libffi-dev &&\ 
    apk add postgresql-dev zlib jpeg-dev jpegoptim optipng

RUN mkdir /config  

ADD requirements.txt /config/  
RUN /bin/sh -c "pip install --no-cache-dir -Ur /config/requirements.txt" && \
    apk del build-deps

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

RUN apk add gettext

RUN mkdir /app && mkdir /app/static && mkdir /app/src
COPY src /app/src
WORKDIR /app/src

COPY entrypoint.sh /
RUN  chmod u+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
