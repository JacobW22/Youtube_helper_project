#!/bin/sh

# Run Gunicorn
echo "Running command: 'celery -A ythelperapp worker -l INFO --without-gossip --without-mingle --without-heartbeat'"
celery -A ythelperapp worker -l INFO --without-gossip --without-mingle --without-heartbeat 