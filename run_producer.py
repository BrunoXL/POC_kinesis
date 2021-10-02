import uvicorn

if __name__ == "run_producer":
    def start():
        # cmd = ["uvicorn", "poc_kinesis.api.producer:app", "--reload"]
        # subprocess.run(cmd)
        uvicorn.run("poc_kinesis.api.producer:app", port=8000)