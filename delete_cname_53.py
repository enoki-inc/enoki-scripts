import boto3

def lambda_handler(event, context):
    # Replace the following with your own values
    hosted_zone_id = 'hosted-zone-id'
    cname_record_name = 'cname-record-name'

    # Create a Route 53 client
    route53_client = boto3.client('route53')

    # Get the current CNAME record
    response = route53_client.list_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        StartRecordName=cname_record_name,
        StartRecordType='CNAME',
        MaxItems='1'
    )

    # Delete the CNAME record
    if 'ResourceRecordSets' in response and len(response['ResourceRecordSets']) > 0:
        record_set = response['ResourceRecordSets'][0]
        response = route53_client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'DELETE',
                        'ResourceRecordSet': record_set
                    }
                ]
            }
        )
        return response
    else:
        return {"message": "CNAME record not found"}

