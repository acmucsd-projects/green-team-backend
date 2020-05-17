import boto3
from botocore.client import Config
from botocore import UNSIGNED
import os

def upload_file(file_name):
    bucket = os.environ["AWS_S3_BUCKET"]
    object_name = "bit-byte/profiles/" + file_name
    
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
    )
    
    s3_client.upload_file('/tmp/' + file_name, bucket, object_name)

    config = Config(signature_version=UNSIGNED)
    config.signature_version = UNSIGNED
    profile_url = boto3.client('s3', config=config).generate_presigned_url('get_object', ExpiresIn=0, Params={'Bucket': bucket, 'Key': object_name})
    
    return profile_url