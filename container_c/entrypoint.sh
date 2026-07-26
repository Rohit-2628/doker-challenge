#!/bin/bash
python3 /opt/server_c.py &
rm -f /sock_data/.sys.sock
socat UNIX-LISTEN:/sock_data/.sys.sock,fork,mode=777 TCP:127.0.0.1:8080
