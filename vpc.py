import boto3

client = boto3.client('VPCs',region_name="us-east-1",aws_access_key_id="AKIA4MUYKIHTBKP7UGUR",aws_secret_access_key="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")

response_var = client_var1.describe_vpcs()
print(response_var)
