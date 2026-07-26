FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 socat

COPY server_c.py /opt/server_c.py
COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]

