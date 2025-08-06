import aiosqlite
from fastapi import APIRouter, HTTPException, Query
from models.database import DB_FILE
from models.schemas import PowRequest, NumberRequest, LogEntry
from services.math_service import log_request
from utils.response import api_response
from typing import Optional
import math

router = APIRouter()


@router.get("/")
async def root():
    return api_response(
        {"info": "Welcome to the Math Microservice! Use /docs to explore the API."}
    )


@router.post("/api/pow")
async def pow_function(payload: PowRequest):
    try:
        result = math.pow(payload.base, payload.exponent)
        await log_request("pow", payload.json(), str(result))
        return api_response({"result": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/fibonacci")
async def fibonacci_function(payload: NumberRequest):
    n = payload.n
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    try:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        await log_request("fibonacci", payload.json(), str(a))
        return api_response({"result": a})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/factorial")
async def factorial_function(payload: NumberRequest):
    n = payload.n
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    try:
        result = math.factorial(n)
        await log_request("factorial", payload.json(), str(result))
        return api_response({"result": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/logs")
async def get_logs(operation: Optional[str] = Query(None)):
    query = "SELECT id, operation, input_data, result, timestamp FROM request_logs"
    params = []
    if operation:
        query += " WHERE operation = ?"
        params.append(operation)
    query += " ORDER BY timestamp DESC"

    async with aiosqlite.connect(DB_FILE) as db:
        cursor = await db.execute(query, params)
        rows = await cursor.fetchall()
        data = [
            LogEntry(
                id=row[0],
                operation=row[1],
                input_data=row[2],
                result=row[3],
                timestamp=row[4],
            )
            for row in rows
        ]
        return api_response([entry.model_dump() for entry in data])
