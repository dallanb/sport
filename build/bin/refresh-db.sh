#!/bin/sh

docker exec -it sport bash -c "python manage.py reset_db"
docker exec -it sport bash -c "python manage.py init"