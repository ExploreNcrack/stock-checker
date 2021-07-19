import os

############# MySQL database settings #################

MYSQL_HOST = os.environ.get("STOCK_CHECKER_MYSQL_HOST", None)
MYSQL_PORT = os.environ.get("STOCK_CHECKER_MYSQL_PORT", None)
MYSQL_DB_NAME = os.environ.get("STOCK_CHECKER_MYSQL_DB_NAME", None)
MYSQL_USER = os.environ.get("STOCK_CHECKER_MYSQL_USER", None)
MYSQL_PASSWORD = os.environ.get("STOCK_CHECKER_MYSQL_PASSWORD", None)