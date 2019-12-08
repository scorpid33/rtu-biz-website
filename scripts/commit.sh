#! /bin/bash

docker commit rtu-biz-website_rtu_biz_1 scorpid33/rtu-biz-website
docker commit rtu-biz-website_db_1 scorpid33/rtu-biz-website-db

docker push scorpid33/rtu-biz-website
docker push scorpid33/rtu-biz-website-db
