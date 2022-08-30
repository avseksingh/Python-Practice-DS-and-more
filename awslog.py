import json
import boto3
import datetime

cw_logs = boto3.client('logs', 'us-east-1')
dynamodb_client = boto3.client('dynamodb', 'us-east-1')
response = cw_logs.filter_log_events(
    logGroupName='API-Gateway-Execution-Logs_piq0thf7k5/Dev')

for Event in response["events"]:
    timestamp = int(Event["timestamp"])
    message = str(Event["message"])
    # print(f"{timestamp}:{message}")
    print(datetime.datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'))

