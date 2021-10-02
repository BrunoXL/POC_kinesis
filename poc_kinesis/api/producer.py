from typing import Optional
from fastapi import FastAPI
from poc_kinesis.service.producer_service import producer_service

import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return "Producer is on and running"

@app.post("/messages")
async def send_messages():
    await producer_service()
    return