import boto3
import os
import logging
import asyncio
from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__.split('.')[-1])

class ProducerService:
    STREAM_NAME = 'poc_kinesis_bruno'
    aws_secret: str
    aws_id: str

    try:
        aws_secret = os.environ['AWS_SECRET_ACCESS_KEY']
        aws_id = os.environ['AWS_ACCESS_KEY_ID']
    except Exception as e:
        logger.error(f"Variaveis de ambientes não definidas")
        raise HTTPException(status_code=401, detail=e.args)

    producer = boto3.client('kinesis', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)

    @classmethod
    async def put_record(cls):
        logger.info(f"Pronto para inserir mensagens em {cls.STREAM_NAME}")

        msg_id: int = 0

        while True:
            message: str = f'Teste {msg_id}: enviando mensagem ao kinesis'
            cls.producer.put_record(
                StreamName=cls.STREAM_NAME,
                Data=message,
                PartitionKey='partitionkey')

            await asyncio.sleep(1)
            
            logger.info(f"Mensagem {msg_id} inseridas com sucesso")
            msg_id = msg_id + 1