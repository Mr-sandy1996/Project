import boto3

client = boto3.client('iam',aws_access_key_id="AKIA4MUYKIHTBKP7UGUR",aws_secret_access_key="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")

response = client.list_users()

#print(response['Users'])

for k in response['Users']:
	print(k['UserName'],k['CreateDate'])