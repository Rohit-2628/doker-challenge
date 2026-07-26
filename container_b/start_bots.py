import subprocess
import time
import random
import string
import binascii

STATIC_HEX_2 = "4465636f795661756c7450617373776f7264313233"
STATIC_HEX_3 = "4d61737465724b6579466f72436f6e7461696e657243"

while True:
    # Generate the dynamic token
    raw_token = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    dyn_hex = binascii.hexlify(raw_token.encode()).decode()

    with open('/auth_sync/current_token.txt', 'w') as f:
        f.write(dyn_hex)

    # Launch the custom binaries directly (zero shell noise!)
    subprocess.Popen(["sys_auth", "-s", "-X", "POST", "http://172.20.0.10:8001/api/login", "-d", f"user=guest&token={dyn_hex}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(["vault_sync", "-s", "-X", "POST", "http://172.20.0.10:9000/api/vault/unlock", "-d", f"auth={STATIC_HEX_2}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(["vault_sync", "-s", "-X", "POST", "--unix-socket", "/tmp_sock/.sys.sock", "http://localhost/api/vault/unlock", "-d", f"auth={STATIC_HEX_3}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(45)
