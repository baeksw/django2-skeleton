#!/bin/bash

clear;

echo "DJango Server"

#gunicorn config.wsgi:application --bind=0.0.0.0:8080 --daemon --reload --pid /var/run/sb_emd.pid
cd ..
gunicorn config.wsgi:application --bind=0.0.0.0:8000 --reload --pid ./sb_ems.pid

