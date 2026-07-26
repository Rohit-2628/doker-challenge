# 🎯 CTF Challenge: The Honeyport Heist

## 📖 The Story
You have successfully infiltrated the perimeter network of a secure facility. We have granted you low-privilege SSH access to a compromised worker node (Container B). 

Intelligence suggests that an automated admin bot is routinely logging into the primary vault system. Your objective is to intercept the vault credentials and capture the master flag. Be careful—their network administrators are known to use active decoy systems to trap intruders.

## 🚀 How to Host This CTF
To spin up the challenge environment, you will need Docker and Docker Compose installed on your host machine.

1. Clone this repository.
2. Run the following command to build and start the containers:
   ```bash
   sudo docker compose up --build -d
