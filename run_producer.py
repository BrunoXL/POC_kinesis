import subprocess

# if __name__ == "run_producter":
def start():
    cmd = ["uvicorn", "poc_kinesis.producer:app", "--reload"]
    subprocess.run(cmd)