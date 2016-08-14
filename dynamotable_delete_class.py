import boto3
import botocore
from datetime import datetime
import json
import requests


region = input("> Region? ")
tablename = input("> Table name? ")
region.lower()

class Dynamo(object):
    region_name = ['us-east-1', 'us-west-2', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'sa-east-1']

    def __init__(self, region, tablename):
        self.region = region
        self.tablename = tablename

    def delete_table(self):
        region_state = False
        table_state = False
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

    def increase_dynamo_read_write(self):
        client = boto3.client('cloudwatch')

        #namespace_input = input("> Namespace? :  " )
        #metricname_input = input("> Metric name? : ")

        # call cloudwatch resource
        response = client.get_metric_statistics(
            Namespace = 'dynamo_dash', #dynamo_dash
            MetricName = 'ProvisionedReadCapacityUnits', #ProvisionedReadCapacityUnits
            StartTime = datetime(2016, 8, 6),
            EndTime = datetime.utcnow(),
            Period = 300,
            Statistics = [
                'Sum'
            ],
            Unit = 'Percent'
        )

        datapoints = json.loads(response)

        print(response)
        # ask for namespace?
        # configure cloudwatch resource for dynamo db table
        # if read and/or write usage is over 90 percent, increase read and write capacity by 100

    def s3_compare(self):
        s3 = boto3.resource('s3')

        org_date_input = input('> What month would you like to compare?(format in MM-YYYY) : ')
        date_parse = org_date_input.split("-")
        org_date_month = int(date_parse[0])
        org_date_year = int(date_parse[1])
        prev_date_month = int(date_parse[0]) - 1

        exists = True
        try:
            s3.meta.client.head_bucket(Bucket='pc-invoices')
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                exists = False

        if exists == True:
            self.compare_invoices(org_date_month, prev_date_month, org_date_year)

    def sum(self, compare):
        sum = 0
        for element in compare:
            sum+=element
        print(sum)


    def compare_invoices(self, org_month, prev_month, org_year):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('pc-invoices')
        objects =[]
        link_objects = []
        compare_objects = []

        compare_list = [org_month, prev_month]
        compare_results = []

        link = 'http://pc-invoices.s3-website-us-west-2.amazonaws.com/'

        for month in compare_list:
            for obj in bucket.objects.filter(Prefix='%i/%i/' % (org_year, month)):
                objects.append(obj.key)

            for n in objects:
                if not '.txt' in n:
                    objects.pop(objects.index(n))

            for i in objects:
                link_objects.append(link + i)

            for x in link_objects:
                f = requests.get(x)
                text = int(f.text)
                compare_objects.append(text)

            compare_results.append(sum(compare_objects))
            objects = []
            link_objects = []
            compare_objects = []

        print("Current Month(%i-%i): " %(org_month, org_year) + str(compare_results[0]) )
        print("Previous Month(%i-%i): " %(prev_month, org_year) + str(compare_results[1]))


example = Dynamo('%s' % region, '%s' % tablename)
example.s3_compare()
