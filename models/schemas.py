from pydantic import BaseModel


class PowRequest(BaseModel):
    base: float
    exponent: float


class NumberRequest(BaseModel):
    n: int


class LogEntry(BaseModel):
    id: int
    operation: str
    input_data: str
    result: str
    timestamp: str
