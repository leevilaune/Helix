#!/bin/bash

python_folder="python"

# Killing old processes
pkill -f "$python_folder/webserver.py"
if [ $? -eq 0 ]; then
    echo "$(date) Successfully killed webserver process"
else
    echo "$(date) Failed to kill webserver process"
fi

# Starting webserver.py
nohup python "$python_folder/webserver.py" > "$python_folder/webserver.log" 2>&1 &
if [ $? -eq 0 ]; then
    echo "$(date) Successfully started webserver, logs in $python_folder/webserver.log"
else
    echo "$(date) Failed to start webserver"
fi

# Final confirmation
echo "$(date) Both servers are now running."
