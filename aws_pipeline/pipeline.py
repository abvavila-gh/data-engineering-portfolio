import boto3

def extract_from_s3(bucket, key):
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=key)
    return obj["Body"].read().decode("utf-8")

def transform(data):
    # Transformación dummy
    return data.upper()

def load_to_s3(bucket, key, data):
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=data)

if __name__ == "__main__":
    raw = extract_from_s3("demo-bucket", "input.csv")
    transformed = transform(raw)
    load_to_s3("demo-bucket", "output.csv", transformed)
