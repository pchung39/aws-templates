import boto3
import json



#TODO: REMEMBER MAKE IT WORK FIRST THEN MAKE IT BETTER. DON'T WORRY ABOUT USER INPUT, JUST MAKE IT WORK

class Main(object):

    queue_name = input(' > SQS Queue name? : ')
    aws_service = input(' > Which AWS Service do you need? : ')
    # TODO: if queue name exists, don't create queue, just add the message.
    # TODO: select region, figure out a way to insert region
    message_content = json.dumps({'service': '%s' % aws_service, 'attribute': 'MyBucketBucketBucket'})

    client = boto3.client('sqs')

    client.create_queue(QueueName = queue_name)
    get_queue_url = client.get_queue_url(QueueName = queue_name)
    queue_url = get_queue_url['QueueUrl']
    message = client.send_message(QueueUrl= queue_url, MessageBody = message_content, DelaySeconds = 10)

    # TODO: need user inputs for message body. Should ask separate questions and store them in separate values.
    # TODO: one question for service, other for name for created object need logic for attributes associated with each AWS service
    # TODO: remember to set permissions! (v2)

if __name__ == "__main__":
    Main()
