from typing import Any
from fastapi.responses import JSONResponse


def api_response(
    data: Any,
    message: str = "Success",
    status: str = "ok",
    status_code: int = 200,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"status": status, "message": message, "data": data},
    )
