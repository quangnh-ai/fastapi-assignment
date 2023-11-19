from fastapi import Request
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def not_found_handler(request: Request, exec: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            {
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": exec.detail,
                "request_info": request
            }
        )
    )

def internal_server_error_handler(request: Request, exec: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(
            {
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": exec.detail
            }
        )
    )

def unporcessable_entity_handler(request: Request, exec: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "message": exec.detail
            }
        )
    )