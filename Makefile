DOCKER_COMPOSE_FILE = docker/docker-compose.yml
PROJECT_NAME = oscar-blog

.PHONY: init start stop log

init:
	echo "Pulling latest service blog..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) build --pull blog
	echo "Run latest service db and pip install packages..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) run --rm blog pip install -r requirements.txt

start:
	echo "Pulling latest service blog..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) build --pull blog
	echo "Start docker..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) up -d --build

stop:
	echo "Stop docker..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) stop

log:
	echo "Log docker..."
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) logs -ft