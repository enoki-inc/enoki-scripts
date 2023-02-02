import boto3
import subprocess

def lambda_handler(event, context):
    # Create a Dockerfile
    with open("Dockerfile", "w") as file:
        file.write("FROM ubuntu:18.04\n")
        file.write("RUN apt-get update && apt-get install -y curl\n")
        file.write("CMD curl http://checkip.amazonaws.com\n")
    
    # Build the Docker image
    subprocess.run(["docker", "build", "-t", "checkip", "."])
    
    # Get the task definition client
    ecs = boto3.client('ecs')
    
    # Use the built image in a task definition
    task_definition = ecs.register_task_definition(
        family='checkip-task-definition',
        containerDefinitions=[
            {
                'name': 'checkip-container',
                'image': 'checkip',
                'memory': 128,
                'cpu': 128
            }
        ]
    )
    
    # Return the task definition ARN
    return {
        'TaskDefinitionARN': task_definition['taskDefinition']['taskDefinitionArn']
    }

