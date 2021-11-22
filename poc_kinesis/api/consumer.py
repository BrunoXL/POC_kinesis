from fastapi import FastAPI

from poc_kinesis.service.consumer_service import ConsumerService


app = FastAPI()

@app.get("/")
def read_root():
    return "Consumer is on and running"

@app.get("/messages")
async def read_messages():
    await ConsumerService().read_messages()
    return 