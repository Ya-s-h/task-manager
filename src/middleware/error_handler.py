# app/middlewares/error_handler.py

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR


class CustomErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)

        except ValueError as ve:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={"error": str(ve)}
            )

        except RequestValidationError as ve:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={"error": "Validation error", "details": ve.errors()}
            )

        except Exception as ex:
            # Log here if needed
            return JSONResponse(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                content={"error": "Internal server error", "details": str(ex)}
            )
