import boto3

dynamo_regions = {'us-east-1' : 'https://dynamodb.us-east-1.amazonaws.com',
                'us-west-2' : 'https://dynamodb.us-west-2.amazonaws.com',
                'ap-south-1' : 'https://dynamodb.ap-south-1.amazonaws.com',
                'ap-northeast-2' : 'https://dynamodb.ap-northeast-2.amazonaws.com',
                'ap-southeast-1' : 'https://dynamodb.ap-southeast-1.amazonaws.com',
                'ap-southeast-2' : 'https://dynamodb.ap-southeast-2.amazonaws.com',
                'ap-northeast-1' : 'https://dynamodb.ap-northeast-1.amazonaws.com',
                'eu-central-1' : 'https://dynamodb.eu-central-1.amazonaws.com',
                'eu-west-1' : 'https://dynamodb.eu-west-1.amazonaws.com',
                'sa-east-1' : 'https://dynamodb.sa-east-1.amazonaws.com'}

for n in dynamo_regions:
    dynamodb = boto3.resource('dynamodb', region_name="%s" % n, endpoint_url="%s" % dynamo_regions[n])

    table = dynamodb.create_table(
        TableName='Accounts',
        KeySchema=[
            {
                'AttributeName': 'Account_ID',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'Date',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Account ID',
                'AttributeType': 'N' #this is assuming that the Account ID is comprised of just numbers.
            },
            {
                'AttributeName': 'Date',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 200
        }

    )
    print("Table status:" + " %s " % dynamo_regions[n], table.table_status)
