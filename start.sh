#!/bin/bash

# 1. Dynamic Password Injection (Optional for web platforms)
DYNAMIC_PASS=${CTF_PASSWORD:-"player"}
echo "ctf_player:$DYNAMIC_PASS" | chpasswd

# 2. Start Vault A API in the background
python3 /opt/container_a/server_a.py &

# 3. Start Vault C API in the background
# (If Vault C is actually run by app.py, just change this line to /opt/container_c/app.py)
python3 /opt/container_c/server_c.py &

# 4. Start the Ghost Bot Engine in the background
python3 /opt/container_bot/start_bots.py &

# 5. Start the SSH Server in the foreground (This keeps the container running)
exec /usr/sbin/sshd -D
