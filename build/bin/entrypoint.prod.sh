#!/bin/sh

. ~/.bashrc

pip install -e .

if [ "$DATABASE" = "sport" ]; then
  echo "Waiting for sport..."

  while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi


if [ ! -d "migrations/versions" ]; then
  echo "Directory migrations/versions does not exist."
  init=$(flask db init --directory=migrations)
  case $init in
    *"Error: Directory migrations already exists and is not empty"*)
      echo "Migrations handled elsewhere"
      ;;
    *)
      sed -i '/import sqlalchemy as sa/a import sqlalchemy_utils' migrations/script.py.mako
      flask db migrate --directory=migrations
      flask db upgrade --directory=migrations
      manage init
      manage load
      ;;
  esac
else
  flask db migrate --directory=migrations
  flask db upgrade --directory=migrations
fi

gunicorn --bind 0.0.0.0:5000 manage:app