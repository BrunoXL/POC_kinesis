import subprocess

if __name__ == "run_productor":
    def start():
        cmd = ["uvicorn", "poc_kinesis.productor:app", "--reload"]
        subprocess.run(cmd)