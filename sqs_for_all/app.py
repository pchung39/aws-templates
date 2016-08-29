import boto3
import json
from sqs_for_all import Main
import time
from collections import OrderedDict


class Execute_message():
    def receive_message(self):
        client = boto3.client('sqs')
        response = client.receive_message(QueueUrl = 'https://sqs.us-east-1.amazonaws.com/029737694246/MyQueue')

        raw_response_1 = json.loads(response['Messages'][0]['Body'])
        raw_response_2 = response['Messages'][0]

        self.service = raw_response_1['service']
        self.attribute = raw_response_1['attribute']
        self.receipt = raw_response_2['ReceiptHandle']

        print(self.service, self.attribute, self.receipt)


    def trigger_service(self):
        client = boto3.client('sqs')
        if self.service == 's3':
            s3 = boto3.resource('s3')
            s3.create_bucket(Bucket= self.attribute)
            response = client.delete_message(
                QueueUrl = 'https://sqs.us-east-1.amazonaws.com/029737694246/MyQueue',
                ReceiptHandle = self.receipt
            )
            print('Message deleted')


def hello_world():


    start_time = time.time()
    while True:
        message = Execute_message()
        message.receive_message()
        print('Message received')
        print('Sending message')
        message.trigger_service()
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))

hello_world()
