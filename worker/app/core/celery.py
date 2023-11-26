from redis import Redis
from core import config

cache = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD,
    db=config.REDIS_DB
)

def is_cache_running():
    return True

def is_broker_running():
    return True