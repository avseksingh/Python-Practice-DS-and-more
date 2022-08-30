import boto3
import datetime

cw_logs = boto3.client('logs', 'us-east-1')
dynamodb_client = boto3.client('dynamodb', 'us-east-1')
response = cw_logs.filter_log_events(
    logGroupName='API-Gateway-Execution-Logs_piq0thf7k5/Dev')
ifs = 0
elses = 0
for Event in response["events"]:

    message = (Event["message"])

    if message.find('"statusCode": 200')<0:
        print("Successfull", message)
        ifs +=1
    else:
        # print(message)
        elses +=1
print("If Statement :",ifs)
print("Else Statement :",elses)



    # print(message)
    # print()
    # print()
    # for x in message:
    #     print(x)
