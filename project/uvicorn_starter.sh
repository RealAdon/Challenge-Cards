#!/bin/sh
gunicorn app.main:app --reload --workers 1 --bind 0.0.0.0:5000