import json

# import requests


def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello {first_name} {last_name}, Greetings from aws lambda",
        }),
    }
