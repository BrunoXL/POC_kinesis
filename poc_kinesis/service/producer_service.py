import boto3
import os
import logging
from fastapi import HTTPException

async def producer_service():
    aws_secret: string
    aws_id: string

    try:
        aws_secret = os.environ['AWS_SECRET_ACCESS_KEY']
        aws_id = os.environ['AWS_ACCESS_KEY_ID']
    except Exception as e:
        logging.error(f"Variaveis de ambientes não definidas")
        raise HTTPException(status_code=401, detail=e.args)

    client = boto3.client('kinesis', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
  
