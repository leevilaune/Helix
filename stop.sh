#!/bin/bash

python_folder="python"

# Stopping webserver.py
pkill -f "$python_folder/webserver.py"
if [ $? -eq 0 ]; then
    echo "$(date) Successfully stopped webserver"
else
    echo "$(date) Failed to stop webserver"
fi
