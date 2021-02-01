from __future__ import print_function
import boto3
from decimal import Decimal
import json
import urllib
import uuid
import datetime
import time
import os
import pandas as pd

s3_client = boto3.client('s3')

# --------------- Main handler ------------------
def lambda_handler(event, context):
    '''
    Uses Rekognition APIs to detect text and labels for objects uploaded to S3
    and store the content in DynamoDB.
    '''
    # Log the the received event locally.
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event.
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        obj = s3_client.get_object(Bucket= bucket, Key= key) 
        # get object and file (key) from bucket

        df = pd.read_csv(obj['Body']) # 'Body' is a key word

        print("==================")
        print(df)


        return 'Success'
    except Exception as e:
        print("Error processing object {} from bucket {}. Event {}".format(key, bucket, json.dumps(event, indent=2)))
        raise e
