from __future__ import print_function
import boto3
import json
import logging
import os
import urllib

import pandas as pd

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
account_name = os.environ.get("accountName")
read_prefix = os.environ.get("readPrefix")
write_prefix = os.environ.get("writePrefix")

# --------------- Main handler ------------------
def lambda_handler(event, context):
    '''
    '''
    # Log the the received event locally.
    logger.info("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event.
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    # we read the data only from they keys which contain the read_prefix
    # we read only csv data

    try:
        obj = s3_client.get_object(Bucket= bucket, Key= key) 
        # get object and file (key) from bucket

        df = pd.read_csv(obj['Body']) # 'Body' is a key word

        logger.info(account_name)
        logger.info("==================")
        logger.info(df)


        return 'Success'
    except Exception as e:
        print("Error processing object {} from bucket {}. Event {}".format(key, bucket, json.dumps(event, indent=2)))
        raise e
