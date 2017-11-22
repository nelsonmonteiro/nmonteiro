#!/bin/bash

set -e
LOGFILE=/home/ubuntu/sites/nmonteiro/logs/nmonteiro_gunicorn.access.log
ERRORFILE=/home/ubuntu/sites/nmonteiro/logs/nmonteiro_gunicorn.error.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
TIMEOUT=120

#The below address:port info will be used later to configure Nginx with Gunicorn
ADDRESS=unix:/var/run/nmonteiro.sock

cd /home/ubuntu/sites/nmonteiro/server
source ./env/bin/activate
export PYTHONPATH=$PYTHONPATH:/home/ubuntu/sites/nmonteiro/server/nmonteiro
test -d $LOGDIR || mkdir -p $LOGDIR
exec ./env/bin/gunicorn nmonteiro.configs.production.wsgi:application -w $NUM_WORKERS --bind=$ADDRESS \
--log-level=DEBUG --log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE --timeout $TIMEOUT
