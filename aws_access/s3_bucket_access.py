import boto3
import os
import pandas as pd
import openpyxl

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id=os.environ['access_key_id1'],
    aws_secret_access_key=os.environ['secret_access_key1']
)

# to see the bucket name in aws
for bucket in s3.buckets.all():
    print(bucket.name)

# add the files into the bucket
# s3.Bucket('chandrabucket02').upload_file(Filename='Chandra.xlsx', Key='Chandra_s3.xlsx')
s3.Bucket('chandrabucket01').upload_file(Filename='pandas.zip', Key='pandas_lib.zip')


# to see the files or objects or keys in the particular bucket
# for obj in s3.Bucket('chandrabucket01').objects.all():
#     print(obj.key)

# to read the data from the excel file
def excel_file_access():
    obj = s3.Object('chandrabucket01', 'Chandra_s3.xlsx')
    body = obj.get()['Body'].read()
    get_output = pd.read_excel(body, index_col=0)
    return get_output

# print(excel_file_access())

# to read the data from the text file


def text_file_access():
    obj = s3.Object('chandrabucket01', 'Chandra_s3.txt')
    body = obj.get()['Body'].readlines()
    for line in body:
        print(line)


# print(text_file_access())


def bucket_creation():
    response = s3.create_bucket(
        ACL='private',
        Bucket='chandrabucket02')
    return response

# print(bucket_creation())









