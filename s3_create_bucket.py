import boto3

client = boto3.client('s3')

response = client.create_bucket(
    ACL= 'public-read-write',
    Bucket='MoviesMovies12345'
)
