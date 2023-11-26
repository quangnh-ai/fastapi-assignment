from fastapi import (
    APIRouter, 
    HTTPException,
    status
)
from pydantic import BaseModel
import uuid, datetime, json, pytz

from core import celery
from core.config import (
    TEST_APP_NAME,
    TEST_TASK_NAME
)

class CeleryResult(BaseModel):
    request_id: str = None
    status: str = None
    start_time: str = None
    end_time: str = None
    result: int = None

class CeleryPostResponse(BaseModel):
    request_id: str = None
    status: str
    posted_time: str = None

celery_router = APIRouter()

@celery_router.post(
    "/divide",
    response_model=CeleryPostResponse,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True
)
async def post(a: int, b: int):
    post_time = str(
        datetime.datetime.now(
            pytz.timezone('Asia/Ho_Chi_Minh')
        )
    )
    request_id = str(
        uuid.uuid5(
            uuid.NAMESPACE_OID,
            TEST_APP_NAME + TEST_TASK_NAME + post_time
        )
    )
    try:
        data_result = CeleryResult(
            request_id=request_id,
            status="PROCESSING",
            start_time=post_time
        )
        data_result = json.dumps(data_result.__dict__)
        celery.cache.set(
            request_id,
            data_result
        )
        celery.celery_excutor.send_task(
            name="{app_name}.{task_name}".format(
                app_name=TEST_APP_NAME,
                task_name=TEST_TASK_NAME
            ),
            kwargs={
                'request_id': request_id,
                'data': data_result,
                'a': a,
                'b': b
            }
        )

        return CeleryPostResponse(
            request_id=request_id,
            status="PROCESSING",
            posted_time=post_time
        )
    except Exception as error:
        celery.cache.set(
            request_id,
            json.dumps(
                CeleryResult(
                    status="FAILED"
                )
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error
        )

    
@celery_router.get("/result/{request_id}")
def get_result(
    *,
    request_id: str
):
    try:
        data = celery.cache.get(request_id)
        data = json.loads(data)
        return data
    except:
        if data == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Request ID not found"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )