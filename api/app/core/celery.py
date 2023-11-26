from redis import Redis
from celery import Celery
from core import config

cache = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    password=config.REDIS_PASSWORD
)

celery_excutor = Celery(
    broker=config.RABBITMQ_LINK,
    backend=config.REDIS_LINK
)