# obsolete, replaced by docker-compose

docker build -t nginx-reverse-proxy nginx/
docker build -t vinoso /srv/vinoso/

docker run -d -p 80:80 nginx-reverse-proxy
docker run -d -p 8000:8000 vinoso