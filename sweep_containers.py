import boto3

def lambda_handler(event, context):
    # Create an ECS client
    ecs_client = boto3.client("ecs")
    
    # List all stopped tasks in the cluster
    tasks = ecs_client.list_tasks(cluster="my-cluster", desiredStatus="STOPPED")["taskArns"]
    
    # Deregister the tasks from the cluster
    for task in tasks:
        ecs_client.deregister_task_definition(taskDefinition=task)
    
    # Delete the stopped tasks
    ecs_client.delete_task(cluster="my-cluster", task=task)
    
    # Set up a CloudWatch Events rule to run the function every hour
    events_client = boto3.client("events")
    events_client.put_rule(
        Name="check-for-stopped-tasks",
        ScheduleExpression="rate(1 hour)",
        State="ENABLED"
    )
    events_client.put_targets(
        Rule="check-for-stopped-tasks",
        Targets=[{
            "Id": "sweep-stopped-tasks",
            "Arn": "arn:aws:lambda:us-east-1:123456789012:function:sweep-stopped-tasks"
        }]
    )

