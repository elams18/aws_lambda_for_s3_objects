
import json
import urllib.parse
import boto3
import os
import logging
import requests

log = logging.getLogger(__name__)

s3 = boto3.client('s3')
S3_BUCKET = "imagesbewelldigital"

def lambda_handler(event, context):
    S3_BASE_URL = f"https://{S3_BUCKET}.s3.ap-south-1.amazonaws.com/"
    log.info('Loading function')
    print(requests.get(S3_BASE_URL))
    try:
        log.info(f'Calling out to {S3_BUCKET} bucket to list objects')
        images = s3.list_objects(Bucket=S3_BUCKET, MaxKeys=10)
        response = dict()
        response['response'] = []
        for image in images['Contents']:
            response['response'].append(S3_BASE_URL+image['Key'])
        response['status'] = 200
        response['Content-Type']='application/json; charset=utf-8'
        response['count'] = len(response['response'])
    except Exception as e:
        log.info(e)
        log.info(f'Error getting from bucket {S3_BUCKET}. Make sure they exist and your bucket is in the same region as this function.')
        response['error'] = e
    return(response)
