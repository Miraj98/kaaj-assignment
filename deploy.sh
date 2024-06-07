#!/bin/bash

set -xe

scp requirements.txt kaaj:fastapi-server/
scp app/main.py kaaj:fastapi-server/app/
scp app/db.py kaaj:fastapi-server/app/

ssh kaaj << EOF
./restart.sh
sudo systemctl status kaaj.service
EOF
