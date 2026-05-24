import asyncio
from app.core.database import engine

async def test():
    async with engine.begin() as conn:
        print("DATABASE CONNECTED SUCCESSFULLY")

asyncio.run(test())