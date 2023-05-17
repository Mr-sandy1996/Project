import boto3

client = boto3.client('s3',aws_access_key_id="AKIA4MUYKIHTBKP7UGUR",aws_secret_access_key="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")
buc_resp = client.list_buckets()
#print(buc_resp['Buckets'])

for i in buc_resp['Buckets']:
	print(i['DisplayName'])