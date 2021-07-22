#!/bin/sh

./wait-for-it.sh db:$STOCK_CHECKER_MYSQL_PORT
./wait-for-it.sh redis:6379
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"