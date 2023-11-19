import os

#=========================================================================
#                          API INFORMATION 
#=========================================================================
API_TITLE = os.environ['API_TITLE']
API_OPENAPI_URL = os.environ['API_OPENAPI_URL']
API_DOCS_URL = os.environ['API_DOCS_URL']
API_REDOC_URL = os.environ['API_REDOC_URL']

#=========================================================================
#                          AUTHENTICATE INFORMATION 
#=========================================================================
AUTHENTICATE_SECRET_KEY = os.environ["AUTHENTICATE_SECRET_KEY"]
AUTHENTICATE_ALGORITHM = os.environ["AUTHENTICATE_ALGORITHM"]
AUTHENTICATE_ACCESS_TOKEN_EXPIRE_MINUTES = os.environ["AUTHENTICATE_ACCESS_TOKEN_EXPIRE_MINUTES"]

#=========================================================================
#                          REDIS INFORMATION 
#=========================================================================
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_DB = int(os.environ['REDIS_DB'])
REDIS_LINK = "redis://:{password}@{hostname}:{port}/{db}".format(
    hostname=REDIS_HOST,
    password=REDIS_PASSWORD,
    port=str(REDIS_PORT),
    db=str(REDIS_DB)
)

#=========================================================================
#                          BROKER INFORMATION 
#=========================================================================
RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_PORT = int(os.environ['RABBITMQ_PORT'])
RABBITMQ_USER = os.environ['RABBITMQ_USER']
RABBITMQ_PASSWORD = os.environ['RABBITMQ_PASSWORD']
RABBITMQ_VHOST = os.environ['RABBITMQ_VHOST']
RABBITMQ_LINK = "amqp://{user}:{password}@{hostname}:{port}/{vhost}".format(
    user=RABBITMQ_USER,
    password = RABBITMQ_PASSWORD,
    hostname=RABBITMQ_HOST,
    port=str(RABBITMQ_PORT),
    vhost=RABBITMQ_VHOST
)

#=========================================================================
#                          DATABASE INFORMATION
#=========================================================================
DATABASE_URL = os.environ["DATABASE_URL"]

#=========================================================================
#                          TEST TASK INFORMATION 
#=========================================================================
TEST_APP_NAME=os.environ["TEST_APP_NAME"]
TEST_TASK_NAME=os.environ["TEST_TASK_NAME"]