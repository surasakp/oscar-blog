# Project Django Oscar Blog

Develop blog with Oscar framework

## Start server
```
#"Pulling latest service web_blog..."
docker-compose -f docker/docker-compose.yml build --pull web_blog

#"Run latest service db and pip install packages..."
docker-compose -f docker/docker-compose.yml run --rm web_blog pip install -r requirements.txt

"Run latest service db and migrate database..."
docker-compose -f docker/docker-compose.yml run --rm web_blog python manage.py migrate

#"Start local..."
docker-compose -f docker/docker-compose.yml up --build
```