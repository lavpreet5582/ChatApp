#!/bin/bash
source /home/lavpreetsingh/Desktop/Projects/Chat-App/chat_env/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
exec python /home/lavpreetsingh/Desktop/Projects/Chat-App/NewChat/manage.py runserver 0.0.0.0:8000 || { echo "Failed to start the server"; exit 1; }
