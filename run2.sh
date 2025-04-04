#!/bin/bash

python_folder="python"

# Killing old processes
pkill -f "$python_folder/webserver.py"
if [ $? -eq 0 ]; then
    echo "$(date) Successfully killed webserver process"
else
    echo "$(date) Failed to kill webserver process"
fi

# Ensure the environment is set correctly
export PATH=$PATH:/home/null/.local/bin
export PYTHONPATH=$PYTHONPATH:/home/null/.local/lib/python3.11/site-packages

# Starting webserver.py
nohup python3 "$python_folder/webserver.py" > "$python_folder/webserver.log" 2>&1 &
if [ $? -eq 0 ]; then
    echo "$(date) Successfully started webserver, logs in $python_folder/webserver.log"
else
    echo "$(date) Failed to start webserver"
fi

# Final confirmation
echo "$(date) Both servers are now running."
