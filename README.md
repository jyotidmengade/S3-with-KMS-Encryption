# S3-with-KMS-Encryption
Uploads a file to an S3 bucket using KMS encryption for enhanced security.
pip install boto3
upload_file_with_kms(
    bucket='my-bucket',
    file_path='data/report.csv',
    key='secure/report.csv',
    kms_key_id='your-kms-key-id'
)
Secure file uploads for sensitive data, e.g., billing, reports, or logs.
