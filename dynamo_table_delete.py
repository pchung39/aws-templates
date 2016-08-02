import boto3
import sys
from collections import OrderedDict

def delete_prep():
    region_input = input('> Region name? ')
    region_input.lower()

    table_input = input('> Table name? ')

    dynamo_regions = OrderedDict({'us-east-1' : 'https://dynamodb.us-east-1.amazonaws.com',
                    'us-west-2' : 'https://dynamodb.us-west-2.amazonaws.com',
                    'ap-south-1' : 'https://dynamodb.ap-south-1.amazonaws.com',
                    'ap-northeast-2' : 'https://dynamodb.ap-northeast-2.amazonaws.com',
                    'ap-southeast-1' : 'https://dynamodb.ap-southeast-1.amazonaws.com',
                    'ap-southeast-2' : 'https://dynamodb.ap-southeast-2.amazonaws.com',
                    'ap-northeast-1' : 'https://dynamodb.ap-northeast-1.amazonaws.com',
                    'eu-central-1' : 'https://dynamodb.eu-central-1.amazonaws.com',
                    'eu-west-1' : 'https://dynamodb.eu-west-1.amazonaws.com',
                    'sa-east-1' : 'https://dynamodb.sa-east-1.amazonaws.com'})
    '''protect from mismatched region names'''
    for n in dynamo_regions:
        if region_input == n:
            region_endpoint = dynamo_regions[n]

    delete_table(region_input, region_endpoint, table_input)


def delete_table(region, endpoint, tablename):
    dynamodb = boto3.resource('dynamodb', region_name = '%s' % region, endpoint_url = '%s' % endpoint)
    client = boto3.client('dynamodb', region_name = '%s' % region)

    print ("Checking if table exists")
    client.describe_table(TableName = '%s' % tablename)
    try:
        response = client.delete_table(TableName = '%s' % tablename)
        print('Table exists!')
        print("Table status:" + " %s " % tablename, response.table_status)
    except Exception as e:
        if "Requested resource not found: Table" in str(e):
            print("Table does not exist")

delete_prep()
