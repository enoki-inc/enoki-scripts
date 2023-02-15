import boto3

def lambda_handler(event, context):
    # Replace the following with your own values
    hosted_zone_id = 'hosted-zone-id'
    cname_record_name = 'cname-record-name'
    cname_record_value = 'cname-record-value'

    # Create a Route 53 client
    route53_client = boto3.client('route53')

    # Create the CNAME record
    response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': cname_record_name,
                        'Type': 'CNAME',
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': cname_record_value
                            },
                        ],
                    }
                },
            ]
        }
    )

    return response

