import json
import boto3
import os

TABLE_NAME=os.environ['TABLE_NAME']

dynamo = boto3.cleint('dynamodb')

def lambda_handler(event, context):
    
    for record in event["Records"]:
        payload=record["body"]
        print(payload)
        dynamo.put_item(TableName=TABLE_NAME,Item={'random':payload})
    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
