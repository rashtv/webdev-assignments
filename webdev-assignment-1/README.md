# Web Development Assignment #1

## Pre-requisites

docker network create webdev-net

## Backend

```
docker build -t webdev-assignment-1-backend .

docker run -it --rm -p 8000:8000 --name backend --network webdev-net webdev-assignment-1-backend
```

## Frontend

```
docker build -t webdev-assignment-1-frontend .

docker run -it --rm -p 5173:5173 --name frontend --network webdev-net webdev-assignment-1-frontend
```

