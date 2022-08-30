import boto3

ec2_client = boto3.client('ec2', 'us-east-1')
response = ec2_client.describe_security_groups()

for i in response['SecurityGroups']:
     print(i)
     break