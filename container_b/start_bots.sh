#!/bin/bash
STATIC_HEX_2="4465636f795661756c7450617373776f7264313233" 
STATIC_HEX_3="4d61737465724b6579466f72436f6e7461696e657243"

while true; do
  RAW_TOKEN_1=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 8)
  DYN_HEX_1=$(echo -n "$RAW_TOKEN_1" | xxd -p | tr -d '\n')
  
  echo "$DYN_HEX_1" > /auth_sync/current_token.txt

  sys_auth -s -X POST http://172.20.0.10:8001/api/login -d "user=guest&token=${DYN_HEX_1}" >/dev/null 2>&1 &
  vault_sync -s -X POST http://172.20.0.10:9000/api-vault/unlock -d "auth=${STATIC_HEX_2}" >/dev/null 2>&1 &
  vault_sync -s -X POST --unix-socket /tmp_sock/.sys.sock http://localhost/api/vault/unlock -d "auth=${STATIC_HEX_3}" >/dev/null 2>&1 &

  sleep 15
done
