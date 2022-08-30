# import boto3
#
# ec2 = boto3.client('ec2')
#
# # Retrieves all regions/endpoints that work with EC2
# response = ec2.describe_regions()
# print('Regions:', response['Regions'])
#
# # Retrieves availability zones only for region of the ec2 object
# response = ec2.describe_availability_zones()
# print('Availability Zones:', response['AvailabilityZones'])

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', 'us-east-1a')

try:
    response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
    print(response)
except ClientError as e:
    print(e)