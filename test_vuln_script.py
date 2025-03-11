import boto3
from botocore.exceptions import NoCredentialsError, ClientError

google_cloud_api_key = "AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6"

def list_s3_buckets():
    
    try:
        # Create a session using the dummy credentials
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name="us-east-1"  # Set your desired region
        )
        
        # Create an S3 client
        s3 = session.client('s3')
        
        # List S3 buckets
        response = s3.list_buckets()
        buckets = response.get('Buckets', [])
        
        if not buckets:
            print("No buckets found or credentials are invalid (as expected with dummy keys).")
        else:
            print("Buckets:")
            for bucket in buckets:
                print(f" - {bucket['Name']}")
    
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_s3_buckets()
