import uvicorn

if __name__ == "run_consumer":
    def start():
        uvicorn.run("poc_kinesis.consumer:app", port=8001)