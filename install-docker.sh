sudo apt-get update
sudo curl -sSL https://get.docker.com/ | sh
sudo usermod -a -G docker $(whoami)
sudo systemctl enable docker # Configure Docker to start on boot
sudo service docker start 
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
