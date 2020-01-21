#! /bin/bash
set -e

docker-compose exec rtu_biz sed -i 's/51\.15\.242\.84/localhost\:8083/' /var/www/html/wp-config.php
docker commit -m "$1" rtu-biz-website_rtu_biz_1 scorpid33/rtu-biz-website
docker commit -m "$1" rtu-biz-website_db_1 scorpid33/rtu-biz-website-db
docker-compose exec rtu_biz sed -i 's/localhost\:8083/51\.15\.242\.84/' /var/www/html/wp-config.php

docker push scorpid33/rtu-biz-website
docker push scorpid33/rtu-biz-website-db
