#!/bin/bash

python_folder="python"

pkill -f "$python_folder/api.py"
pkill -f "$python_folder/webserver.py"

nohup python "$python_folder/api.py" > "$python_folder/api.log" 2>&1 &
nohup python "$python_folder/webserver.py" > "$python_folder/webserver.log" 2>&1 &
echo "Both servers are now running."

