import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
# the way we upload user images will be similar to this
with open('test_image.jpg', 'rb') as data:
    s3.Bucket('r33-pixly').put_object(Key='test_image.jpg', Body=data)