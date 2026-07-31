# Use a lightweight Debian-based Python image instead of full Ubuntu
# This eliminates the need to compile Python from scratch during the build
FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# --no-install-recommends prevents downloading unnecessary bloat/documentation
# We only install the bare minimum tools required for the challenge
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    openssh-server \
    nano \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Create the shared directories
RUN mkdir -p /auth_sync /tmp_sock /var/run/sshd

# Setup the player user with a static fallback password
RUN useradd -m -s /bin/bash ctf_player && \
    echo "ctf_player:player" | chpasswd

# Copy all challenge components into the container
COPY container_a/ /opt/container_a/
COPY container_c/ /opt/container_c/
COPY container_bot/ /opt/container_bot/

# Copy and install the victory animation
COPY container_bot/submit_flag.py /usr/local/bin/submit_flag
RUN chmod +x /usr/local/bin/submit_flag

# Copy the master startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose the SSH port for the player
EXPOSE 22

# Boot everything up
CMD ["/start.sh"]
