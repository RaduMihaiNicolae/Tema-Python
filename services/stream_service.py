# services/stream_service.py
import redis.asyncio as redis

redis_client = redis.Redis(host="localhost", port=6379)


async def push_to_stream(operation: str, input_data: str, result: str):
    try:
        await redis_client.xadd(
            "math_operations",
            {"operation": operation, "input": input_data, "result": result},
        )
    except Exception as e:
        print(f"[STREAM ERROR] Failed to push to stream: {e}")
