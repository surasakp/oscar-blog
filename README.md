# Project Django Oscar Blog

Develop blog with Oscar framework

## Start server
```
docker-compose -f docker/docker-compose.yml build --pull web_blog

docker-compose -f docker/docker-compose.yml run --rm web_blog pip install -r requirements.txt

docker-compose -f docker/docker-compose.yml run --rm web_blog python manage.py migrate

docker-compose -f docker/docker-compose.yml up --build
```