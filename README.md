# URL_Shortener_Service

The application uses the following software stack deployed in Docker, tested with Ubuntu 18.04.6 LTS:
- Frontend: ReactJS
- Backend: Django
- Database: Postgres

# Prerequistes and Setup
To install Docker, run the following commands:
1. sudo apt-get update
2. sudo apt-get install ca-certificates curl gnupg lsb-release
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4. echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5. sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose
6. sudo groupadd docker
7. sudo usermod -aG docker $USER

To deploy the project on local machine, download/clone the repository to the local machine, and run the command sudo docker-compose up --build
