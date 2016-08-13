import boto3

client = boto3.client('cloudwatch')

response = client.get_metric_statistics(
    Namespace='string',
    MetricName='ConsumedReadCapacityUnits',
    Dimensions=[
        {
            'Name': 'Time',
            'Value': 'Percent'
        },
    ],
    StartTime=datetime(2016, 1, 1),
    EndTime=datetime(2016, 7, 26),
    Period=60,
    Statistics=[
        'Minimum'|'Maximum'
    ],
    Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
)
