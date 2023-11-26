import json
import datetime
import pytz
from celery import (
    Celery,
    Task
)

from core import celery
from core import config

app = Celery(
    config.TEST_APP_NAME,
    broker=config.RABBITMQ_LINK,
    backend=config.REDIS_LINK
)


@app.task(
    name="{app_name}.{task_name}".format(
        app_name=config.TEST_APP_NAME,
        task_name=config.TEST_TASK_NAME
    )
)
def test_task(
    request_id: str,
    data: bytes,
    a: int,
    b: int
):  
    data = json.loads(data)
    try:
        data['result'] = a/b
        data['end_time'] = str(
            datetime.datetime.now(
                pytz.timezone('Asia/Ho_Chi_Minh')
            )
        )
        data['status'] = "SUCCESSED"
        celery.cache.set(
            request_id,
            json.dumps(data)
        )
    except Exception as e:
        data['status'] = 'FAILED'
        data['message'] = str(e)
        data['end_time'] = str(
            datetime.datetime.now(
                pytz.timezone('Asia/Ho_Chi_Minh')
            )
        )
        celery.cache.set(
            request_id,
            json.dumps(data)
        )
