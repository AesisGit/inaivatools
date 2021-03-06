#!/bin/sh
ssh root@157.230.127.167 <<EOF
    source ./inaivatoolsenv/bin/activate
    cd inaivatools
    git pull
    pip install -r requirements.txt
    ./manage.py migrate
    systemctl restart gunicorn
    systemctl daemon-reload
    systemctl restart gunicorn.socket gunicorn.service
    nginx -t && sudo systemctl restart nginx
    exit
EOF