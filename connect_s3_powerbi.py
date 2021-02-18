import boto3, os, io
import pandas as pd 

my_key= 'INSERT_AWS_KEY_HERE' 
my_secret= 'INSERT_AWS_SECRET_HERE' 

my_bucket_name = 'mytestbucketpbi' 
my_file_path = 'mysubfolder/heart_disease.csv' 

session = boto3.Session(aws_access_key_id=my_key,aws_secret_access_key=my_secret) 
s3Client = session.client('s3') 
f = s3Client.get_object(Bucket=my_bucket_name, Key=my_file_path) 
heart_disease_data = pd.read_csv(io.BytesIO(f['Body'].read()), header=0) 
