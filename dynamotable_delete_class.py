import boto3
import sys

region = input("> Region? ")
tablename = input("> Table name? ")
region.lower()

class Dynamo(object):

    region_name = ['us-east-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'sa-east-1']

    def __init__(self, region, tablename):
        self.region = region
        self.tablename = tablename

    def delete_table(self):
        print("Checking if region exists...")
        for n in Dynamo.region_name:
            if region == n:
                region_state = True
                print("We found region: '%s'" % region)
                break

        if region_state == True:
            client = boto3.client('dynamodb', region_name = '%s' % self.region)
            print ("Checking if table exists...")
            try:
                description = client.describe_table(TableName = '%s' % self.tablename)
                table_state = True
                print('Table exists!')
            except Exception as e:
                if "Requested resource not found: Table" in str(e):
                    table_state = False
                    print("Table does not exist")
        else:
            print("Please validate the region before proceeding!")

        if region_state == True & table_state == True:
            print("Deleting Table!")
            delete_response = client.delete_table(TableName = '%s' % tablename)
            waiter = client.get_waiter('table_not_exists')
            if waiter == True:
                print("Table deleted!")

example = Dynamo('%s' % region, '%s' % tablename)
example.delete_table()
