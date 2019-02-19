FROM alpine:3.8

# MAINTAINER "anywon"

WORKDIR /home/anywon

# Make User 
RUN adduser -D anywon && chown -R anywon:anywon /home/anywon && \
mkdir /home/anywon/supervisor && mkdir /home/anywon/web_server

# Package Update
RUN apk update && apk upgrade && \
    apk add gcc make musl-dev supervisor python3 python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY files/pylib/requirements.txt /home/anywon/ 
COPY files/conf/supervisord.conf /home/anywon/supervisor

RUN rm /etc/supervisord.conf && ln -s /home/anywon/supervisor/supervisord.conf /etc/

# python code
COPY web_server/ /home/anywon/web_server

RUN pip3.6 install -r /home/anywon/requirements.txt

# Remove
RUN apk del gcc make
