#!/bin/bash

python_folder="python"

# Killing old processes
pkill -f "$python_folder/api.py"
if [ $? -eq 0 ]; then
    echo "$(date) Successfully killed api process"
else
    echo "$(date) Failed to kill api process"
fi

pkill -f "$python_folder/webserver.py"
if [ $? -eq 0 ]; then
    echo "$(date) Successfully killed webserver process"
else
    echo "$(date) Failed to kill webserver process"
fi

# Starting api.py
nohup python "$python_folder/api.py" > "$python_folder/api.log" 2>&1 &
if [ $? -eq 0 ]; then
    echo "$(date) Successfully started api, logs in $python_folder/api.log"
else
    echo "$(date) Failed to start api"
fi

# Starting webserver.py (without tee)
nohup python "$python_folder/webserver.py" > "$python_folder/webserver.log" 2>&1 &
if [ $? -eq 0 ]; then
    echo "$(date) Successfully started webserver, logs in $python_folder/webserver.log"
else
    echo "$(date) Failed to start webserver"
fi

# Final confirmation
echo "$(date) Both servers are now running."
