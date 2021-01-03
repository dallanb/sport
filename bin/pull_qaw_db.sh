#!/bin/bash

ssh -i /home/dallanbhatti/.ssh/github super_dallan@mega <<EOF
  docker exec sport_db pg_dump -c -U "$1" sport > sport.sql
EOF
rsync -chavzP --stats --remove-source-files super_dallan@mega:/home/super_dallan/sport.sql "$HUNCHO_DIR"/services/sport/sport.sql

docker exec -i sport_db psql -U "$1" sport <"$HUNCHO_DIR"/services/sport/sport.sql
