import boto3
import os
import logging

from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__.split('.')[-1])


class ConsumerService:
    AWS_ARN: str = 'arn:aws:kinesis:us-east-1:893777461466:stream/poc_kinesis_bruno'
    STREAM_NAME: str = 'poc_kinesis_bruno'

    aws_secret: str
    aws_id: str

    try:
        aws_secret = os.environ['AWS_SECRET_ACCESS_KEY']
        aws_id = os.environ['AWS_ACCESS_KEY_ID']
    except Exception as e:
        logger.error(f"Variaveis de ambientes não definidas")
        raise HTTPException(status_code=401, detail=e.args)

    consumer = boto3.client('kinesis', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)

    @classmethod
    async def read_messages(cls):
        register_response = cls.consumer.register_stream_consumer(
            StreamARN=cls.AWS_ARN,
            ConsumerName='Consumer'
        )

        print(register_response)

        shardList = cls.consumer.list_shards(StreamName=cls.STREAM_NAME)

        result = cls.consumer.subscribe_to_shard(
            ConsumerARN=register_response.Consumer.ConsumerARN,
            ShardId=shardList[0].ShardId,
            StartingPosition={
                'Type': 'AT_SEQUENCE_NUMBER'
            }
        )

        print(result)

        cls.consumer.deregister_stream_consumer(
                    StreamARN=cls.AWS_ARN,
                    ConsumerName='Consumer',
                    ConsumerARN=register_response.ConsumerARN
        )