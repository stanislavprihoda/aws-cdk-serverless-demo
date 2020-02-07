import json
import random
import boto3
import os

QUEUE_URL=os.environ['QUEUE_URL']

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    random_num=str(random.randint(0,10000))
    print(QUEUE_URL, random_num)
    resp = sqs.send_message(QueueUrl=QUEUE_URL,MessageBody=random_num)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully published message: {random_num}, with id: {resp["MessageId"]}.')
    }