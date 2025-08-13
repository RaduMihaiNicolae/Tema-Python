from datetime import datetime
from models.database import DB_FILE
import aiosqlite
from services.stream_service import push_to_stream


async def log_request(operation: str, input_data: str, result: str):
    timestamp = datetime.now().isoformat()
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute(
            "INSERT INTO request_logs (operation, input_data, result, timestamp) VALUES (?, ?, ?, ?)",
            (operation, input_data, result, timestamp),
        )
        await db.commit()

    await push_to_stream(operation, input_data, result)
