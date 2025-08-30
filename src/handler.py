import json
import boto3

s3 = boto3.client('s3')
dynamo_client = boto3.resource('dynamodb')

def process_data(event, context):
    body = json.loads(event['body'])
    data = body.get('data')
    bucket_name = 'my-serverless-data-pipeline-bucket'
    table_name = 'DataTable'
    
    # Upload data to S3
    s3.put_object(Bucket=bucket_name, Key='data.json', Body=json.dumps(data))
    
    # Store data to DynamoDB
    table = dynamo_client.Table(table_name)
    table.put_item(Item={'id': '1', 'data': data})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data processed successfully'})
    }
