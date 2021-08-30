import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Consumer is on and running"

@app.get("/messages")
def read_messages():
    return 