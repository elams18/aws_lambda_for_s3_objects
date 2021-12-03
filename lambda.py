
import json
import urllib.parse
import boto3
import os
import logging

log = logging.getLogger(__name__)

s3 = boto3.client('s3')
S3_BUCKET = "imagesbewelldigital"

def lambda_handler(event, context):
    REGION = event['Records'][0]['awsRegion']
    S3_BASE_URL = f"https://{S3_BUCKET}.s3.{REGION}.amazonaws.com/"
    log.info('Loading function')
    
    try:
        log.info(f'Calling out to {S3_BUCKET} bucket to list objects')
        images = s3.list_objects(Bucket=S3_BUCKET, MaxKeys=10)
        response = dict()
        response['response'] = []
        for image in images['Contents']:
            response['response'].append(S3_BASE_URL+image['Key'])
    except Exception as e:
        log.info(e)
        log.info(f'Error getting from bucket {S3_BUCKET}. Make sure they exist and your bucket is in the same region as this function.')
        raise e
    return(response)
