FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install optipng jpegoptim
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
COPY src/ /app/
COPY entrypoint.sh /
RUN  chmod u+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
