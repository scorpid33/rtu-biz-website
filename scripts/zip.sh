#! /bin/bash
set -e

rm -f rtu-biz-website.img rtu-biz-website-db.img deliverable.7z

docker pull scorpid33/rtu-biz-website
docker save -o rtu-biz-website.img scorpid33/rtu-biz-website

docker pull scorpid33/rtu-biz-website-db
docker save -o rtu-biz-website-db.img scorpid33/rtu-biz-website-db

7z a \
	deliverable.7z \
	docker-compose.yml \
	README.md \
	rtu-biz-website.img \
 	rtu-biz-website-db.img
