import os
import math
import boto3
from boto3.s3.transfer import TransferConfig

def upload_large_file_to_s3(file_path, bucket_name, object_name, access_key, secret_key, endpoint_url):
    # Initialize S3 client with custom endpoint and credentials
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key,
                             endpoint_url=endpoint_url)

    # Configuration for multipart upload
    GB = 1024 ** 3
    config = TransferConfig(multipart_threshold=5 * GB, max_concurrency=10,
                            multipart_chunksize=100 * 1024 * 1024, use_threads=True)

    # Get the file size
    file_size = os.path.getsize(file_path)

    # Determine how many parts the file will be split into
    part_count = math.ceil(file_size / config.multipart_chunksize)

    print(f"Uploading {file_path} to {bucket_name}/{object_name}")
    print(f"File size: {file_size / (1024 ** 2):.2f} MB, Parts: {part_count}")

    # Upload the file
    try:
        s3_client.upload_file(file_path, bucket_name, object_name, Config=config)
        print("Upload completed successfully!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Example parameters, you can replace these with your own values or pass them from command-line arguments
    file_path = os.getenv('FILE_PATH')
    bucket_name = os.getenv('S3_BUCKET')
    object_name = os.getenv('OBJECT_NAME')
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    endpoint_url = os.getenv('S3_ENDPOINT')

    upload_large_file_to_s3(file_path, bucket_name, object_name, access_key, secret_key, endpoint_url)
