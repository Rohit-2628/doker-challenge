FROM ubuntu:22.04

RUN apt-get update && apt-get install -y openssh-server curl procps python3 && \
    mkdir /var/run/sshd

# Clone curl to make quiet, custom-named binaries
RUN cp /usr/bin/curl /usr/bin/sys_auth && \
    cp /usr/bin/curl /usr/bin/vault_sync

RUN useradd -ms /bin/bash ctf_player && \
    echo 'ctf_player:player123' | chpasswd

# The massive Binary ASCII Art Banner
RUN cat << 'BANNER' > /etc/profile.d/motd.sh
#!/bin/bash
echo -e "\033[32m"
echo "0101010101010101010101010101010101010101010101010101010101010"
echo "10                                                         01"
echo "01  100  001 110   00 110      000111 0001111 110  001     10"
echo "10  010  010 0110  11 011      011  1 011     011 010      01"
echo "01  110  011 11010 00 110      110  0 110     111110       10"
echo "10  011  110 011 0111 011      011  1 011     011 010      01"
echo "01  01100110 110   00 11011111 110001 1100000 110  001     10"
echo "10                                                         01"
echo "01      110   001   001   110   00 110      111111111      10"
echo "10      011   110  01110  011   11 011         011         01"
echo "01      110   001 001 110 110   00 110         001         10"
echo "10       011 110  1111111  011 110 011         110         01"
echo "01        11001   001 110   01110  11011111    001         10"
echo "10                                                         01"
echo "0101010101010101010101010101010101010101010101010101010101010"
echo -e "\033[0m"
echo "                       Find the flag."
echo ""
BANNER
RUN chmod +x /etc/profile.d/motd.sh

RUN curl -L -o /usr/local/bin/pspy https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64 && \
    chmod +x /usr/local/bin/pspy

COPY start_bots.py /opt/start_bots.py

# Launch using Python instead of Bash
ENTRYPOINT python3 /opt/start_bots.py & /usr/sbin/sshd -D
