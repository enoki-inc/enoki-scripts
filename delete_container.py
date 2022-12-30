import boto3

def lambda_handler(event, context):
    # Extract the task ARN from the event data
    task_arn = event["task_arn"]
    
    # Create an ECS client
    ecs_client = boto3.client("ecs")
    
    # Delete the task
    ecs_client.stop_task(cluster="my-cluster", task=task_arn)
    ecs_client.delete_task(cluster="my-cluster", task=task_arn)

