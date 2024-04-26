sudo docker build --no-cache . -t backend-app:latest
poetry export -f requirements.txt --without-hashes > requirements.txt
sudo docker-compose up 