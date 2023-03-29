# score-setup
Scripts to setup the S3 layout that Score requires

Set the following environment variables:

ACCESS_KEY - the S3 access key
SECRET_KEY - the S3 secret key
S3_URL - the URL to the S3 service

and export them. Then run `initialize_score.py`. The script requires the
[boto3](https://aws.amazon.com/sdk-for-python/) library.

