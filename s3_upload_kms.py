import boto3

def upload_file_with_kms(bucket, file_path, key, kms_key_id, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)
    with open(file_path, 'rb') as data:
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=data,
            ServerSideEncryption='aws:kms',
            SSEKMSKeyId=kms_key_id
        )
    print(f"Uploaded {file_path} to {bucket}/{key} with KMS encryption.")

# upload_file_with_kms('my-bucket', 'sample.txt', 'uploads/sample.txt', 'your-kms-key-id')
