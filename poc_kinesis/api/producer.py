from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Producer is on and running"

@app.post("/messages")
def send_messages():
    return