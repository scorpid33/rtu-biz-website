# rtu-biz-website

## Setup

1. Install Docker
2. Install docker-compose
3. Install 7zip

## Build and run image

1. Decompress images.7z
2. `docker load -i rtu-biz-website.img`
3. `docker load -i rtu-biz-website-db.img`
5. `docker-compose up`
6. Navigate to http://localhost:8083/wp-admin/

## Reset current container

`docker-compose down`
