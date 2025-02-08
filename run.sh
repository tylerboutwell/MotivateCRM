#!/bin/bash
set -e
gunicorn crm_project.wsgi --log-file -