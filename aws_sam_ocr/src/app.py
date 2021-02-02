from __future__ import print_function
import boto3
import json
import logging
import os
import urllib

from io import StringIO

import pandas as pd

from validate import validate

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
account_name = os.environ.get("accountName")
read_prefix = os.environ.get("readPrefix")
write_prefix = os.environ.get("writePrefix")
string_columns = os.environ.get("stringColumns")
# converting string_columns to a list
string_columns = string_columns.split(",")

# --------------- Main handler ------------------
def lambda_handler(event, context):
    '''
    This function handles the S3 cloudwatch event, checks if there is NPI data
    in the S3 file uploaded, if there is no NPI data it is written back to the
    write_prefix
    '''
    # Log the the received event locally.
    logger.info("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event.
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        obj = s3_client.get_object(Bucket= bucket, Key= key) 
        # get object and file (key) from bucket

        df = pd.read_csv(obj['Body']) # 'Body' is a key word
        is_valid = validate(df, string_columns)

        logger.info("==================")
        logger.info(account_name)
        logger.info(is_valid)

        # if valid we write the data back to S3
        if is_valid:
            # writing the data back in write_prefix location using csv buffer
            to_write_key = key.replace(read_prefix, write_prefix)
            csv_buffer = StringIO()
            df.to_csv(csv_buffer)
            s3_client.put_object(
                    Bucket= bucket,
                    Key= to_write_key,
                    Body=csv_buffer.getvalue()
                )

            return 'Success'
        else:
            return 'The data is not valid'

    except Exception as e:
        print("Error processing object {} from bucket {}. Event {}".format(key, bucket, json.dumps(event, indent=2)))
        raise e
