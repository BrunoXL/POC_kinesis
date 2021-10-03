import boto3
import os
import logging
from fastapi import HTTPException

async def producer_service():
    aws_secret: str
    aws_id: str
    STREAM_NAME: 'poc_lambda_bruno'

    try:
        aws_secret = os.environ['AWS_SECRET_ACCESS_KEY']
        aws_id = os.environ['AWS_ACCESS_KEY_ID']
    except Exception as e:
        logging.error(f"Variaveis de ambientes não definidas")
        raise HTTPException(status_code=401, detail=e.args)

    producer = boto3.client('kinesis', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)

    message: str = 'Teste: enviando menssagem ao kinesis'

    producer.put_record(
        StreamName=STREAM_NAME,
        Data=message,
        PartitionKey='partitionkey')


def encode_messages(message):
    return str.encode(message)
