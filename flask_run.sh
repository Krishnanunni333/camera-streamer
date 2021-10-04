#!/usr/bin/env bash

sudo cat >/etc/systemd/system/my-service.service <<EOL
[Unit]
Description=Flask startup script

[Service]
ExecStart=/home/transang/flask.sh start

[Install]
WantedBy=default.target.target
EOL
