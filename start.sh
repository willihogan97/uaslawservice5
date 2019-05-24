#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn server5.wsgi:application \
    --bind 0.0.0.0:21920 \
    --workers 3