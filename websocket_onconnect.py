import json
import boto3
import botocore

def lambda_handler(event, context):
    
    connectionId = event["requestContext"]["connectionId"]
    userId = event["queryStringParameters"]["userid"]
    print(connectionId)
    print(userId)
    print(event)
    dynamo = boto3.resource('dynamodb').Table("OnlineConnection")
    jsonobj = {
        "UserID":userId,
        "token":connectionId
    }
    dynamo.put_item(Item = jsonobj)
    
    
    
    return{
        "isBase64Encoded": False,
        "statusCode":200,
        "headers":{"status":"success"},
        "body":"success"
    }