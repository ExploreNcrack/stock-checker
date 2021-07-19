# fill your environment variables and execute this file to set up the database config

# for windows powershell
# for running on local machine, STOCK_CHECKER_MYSQL_HOST=localhost
$env:STOCK_CHECKER_MYSQL_HOST = ''
# usually the port for mysql is 3306
$env:STOCK_CHECKER_MYSQL_PORT = ''
$env:STOCK_CHECKER_MYSQL_DB_NAME = ''
$env:STOCK_CHECKER_MYSQL_USER = ''
$env:STOCK_CHECKER_MYSQL_PASSWORD = ''

$env:MYSITE_SECRET_KEY = ''
# False for production
$env:DEBUG = ''
# Leave empty will used default as True
$env:CORS_ALLOW_ALL = ''
$env:DJANGO_LOG_LEVEL = ''