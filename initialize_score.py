#!/usr/bin/env python3

import logging
import os
import sys
from http.client import HTTPConnection
from io import StringIO
# HTTPConnection.debuglevel = logging.DEBUG

import boto3
from botocore.exceptions import ClientError

access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')
url = os.getenv('S3_URL')

s3 = boto3.client('s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=url,
)

s3r = boto3.resource('s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=url,
)

buckets = ['apa', 'score-state']
for bucket_name in buckets:
    bucket = s3r.Bucket(bucket_name)
    try:
        bucket.create()
        print("created:", bucket)
    except ClientError as e:
        print(f"Failed to create bucket {bucket_name}: {e}", file=sys.stderr)

# # Add an image to the bucket
bucket = s3r.Bucket('apa')
bucket.put_object(Body=b'nothingherebutuschickens', Key='score/sentinel')
#bucket = s3r.Bucket('score-state')
#bucket.put_object(Body=b'nothingherebutuschickens', Key='marker')

response = s3.list_buckets()
for bucket_dict in response['Buckets']:
    print(f'    {bucket_dict["Name"]}')

for obj in bucket.objects.all():
    print(' ->', obj)

