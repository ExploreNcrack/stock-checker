import os

############# MySQL database settings #################

MYSQL_HOST = os.environ.get("STOCK_CHECKER_MYSQL_HOST", None)
MYSQL_PORT = os.environ.get("STOCK_CHECKER_MYSQL_PORT", None)
MYSQL_DB_NAME = os.environ.get("STOCK_CHECKER_MYSQL_DB_NAME", None)
MYSQL_USER = os.environ.get("STOCK_CHECKER_MYSQL_USER", None)
MYSQL_PASSWORD = os.environ.get("STOCK_CHECKER_MYSQL_PASSWORD", None)

############# email settings #################

MAIL_HOST = os.environ.get("STOCK_CHECKER_EMAIL_HOST", None)
MAIL_USE_TLS = os.environ.get("STOCK_CHECKER_EMAIL_USE_TLS", None)
MAIL_PORT = os.environ.get("STOCK_CHECKER_EMAIL_PORT", None)
MAIL_HOST_USER = os.environ.get("STOCK_CHECKER_EMAIL_HOST_USER", None)
MAIL_HOST_PASSWORD = os.environ.get("STOCK_CHECKER_EMAIL_HOST_PASSWORD", None)

############# celery settings #################

CELERY_BROKER = os.environ.get("STOCK_CHECKER_CELERY_BROKER_URL", None)