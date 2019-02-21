# Visitors Counter

1. Run docker-compose up --build[optional].
2. Creates two separate containers redis as in-memory database and python app client that communicates with redis to store/ retrieve visitors count.
3. Docker compose automates the builds for multiple containers (redis-server and python app).
4. Try to hit the request from browser using "Docker-ip:port" (Windows Home edition should use Docker server ip generated from your docker toolbox terminal).
