import boto3
import sys

class Dynamo_Table():
    self.region = input("> Region? ")
    self.tablename = input("> Table name? ")
    self.region.lower()

    region_state = False
    tablename_state = False
    region_name = ['us-east-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'sa-east-1']

    def validate_region(self):
        for n in region_name:
            if self.region == n:
                region_state = True
                return region_state
            else:
                region_state = False

    def validate_table(self):
        if region_state = True:
            client = boto3.client('dynamodb', region_name = '%s' % self.region)
            print ("Checking if table exists")
            try:
                description = client.describe_table(TableName = '%s' % tablename_input)
                table_state = True
                print('Table exists!')
            except Exception as e:
                if "Requested resource not found: Table" in str(e):
                    table_state = False
                    print("Table does not exist")
        else:
            print("Please validate the region before proceeding!")

    def delete_table(self):
        if table_state && region_state == True:
            '''working on this'''
