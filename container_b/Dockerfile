FROM ubuntu:22.04

# Install base tools and setup SSH (Removed the -u 1000 flag)
RUN apt-get update && apt-get install -y openssh-server curl nano procps && \
    mkdir /var/run/sshd && \
    useradd -rm -d /home/ctf_player -s /bin/bash ctf_player && \
    echo 'ctf_player:player123' | chpasswd

# Inject the massive terminal intro into the player's .bashrc
RUN echo 'echo -e "\033[36m"' >> /home/ctf_player/.bashrc && \
    echo 'echo " ██████╗████████╗███████╗"' >> /home/ctf_player/.bashrc && \
    echo 'echo "██╔════╝╚══██╔══╝██╔════╝"' >> /home/ctf_player/.bashrc && \
    echo 'echo "██║        ██║   █████╗  "' >> /home/ctf_player/.bashrc && \
    echo 'echo "██║        ██║   ██╔══╝  "' >> /home/ctf_player/.bashrc && \
    echo 'echo "╚██████╗   ██║   ██║     "' >> /home/ctf_player/.bashrc && \
    echo 'echo " ╚═════╝   ╚═╝   ╚═╝     "' >> /home/ctf_player/.bashrc && \
    echo 'echo -e "\033[0m"' >> /home/ctf_player/.bashrc && \
    echo 'echo "Welcome to the internal network. Find the hidden vaults."' >> /home/ctf_player/.bashrc && \
    echo 'echo ""' >> /home/ctf_player/.bashrc

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
