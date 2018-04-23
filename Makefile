DOCKER_COMPOSE_FILE = docker/docker-compose.yml
PROJECT_NAME = webblog

.PHONY: init start stop log

init:
	echo "Pulling latest service web_blog..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) build --pull web_blog
	echo "Run latest service db and pip install packages..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) run --rm web_blog pip install -r requirements.txt

start:
	echo "Pulling latest service web_blog..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) build --pull web_blog
	echo "Start docker..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) up -d --build

stop:
	echo "Stop docker..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) stop

log:
	echo "Log docker..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) logs -ft
