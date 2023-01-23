import boto3
iam = boto3.client('iam')

#Creating user
response = iam.create_user(
    UserName = 'Tron2k'
)
print(response)