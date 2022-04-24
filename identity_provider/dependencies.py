import os
import motor.motor_asyncio


async def db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db = client.college
    return db
