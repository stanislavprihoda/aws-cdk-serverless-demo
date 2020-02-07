import json
import random
import boto3

QUEUE_URL=os.environ['QUEUE_URL']
TABLE_NAME=os.environ['TABLE_NAME']

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    _random=str(random.randint(0,10000))
    resp = sqs.send_message(QueueUrl=QUEUE_URL,MessageBody=_random)
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully published message: {_random}, with id: {resp["MessageId"]}.')
    }
