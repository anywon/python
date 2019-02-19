#!/bin/bash

docker run -d -it --name web_server --pid="host" --net="host" \
                  --restart="always" --ulimit nofile=200000:200000 \
                  -v /etc/localtime:/etc/localtime:ro \
                  web_server:1.0 \
                  /usr/bin/supervisord
