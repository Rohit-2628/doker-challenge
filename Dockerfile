FROM ubuntu:22.04

# Avoid timezone/keyboard prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install all necessary tools for the APIs and the player
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    openssh-server \
    nano \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Create the shared directories (replacing Docker volumes)
RUN mkdir -p /auth_sync /tmp_sock /var/run/sshd

# Setup the player user with a static fallback password
RUN useradd -m -s /bin/bash ctf_player && \
    echo "ctf_player:player" | chpasswd

# Copy all challenge components into the container
COPY container_a/ /opt/container_a/
COPY container_c/ /opt/container_c/
COPY container_bot/ /opt/container_bot/

# Copy and install the victory animation
COPY container_b/submit_flag.py /usr/local/bin/submit_flag
RUN chmod +x /usr/local/bin/submit_flag

# Copy the master startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose the SSH port for the player
EXPOSE 22

# Boot everything up
CMD ["/start.sh"]
