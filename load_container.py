#lambda function for "loading" container with the appropriate docker image and with the minimum recommend pc specs"

#example use case
#curl -X POST -H "Content-Type: application/json" -d '{
#    "container_name": "aither",
#    "image_name": "enokiinc/aither",
#    "cluster_arn": "arn:aws:ecs:us-east-1:123456789012:cluster/aither-cluster"
#}' https://lambda-function-url


import boto3

def lambda_handler(event, context):
    # Create an ECS client
    ecs_client = boto3.client("ecs")
    
    # Extract the container name, image name, and cluster ARN from the event data
    container_name = event["container_name"]
    image_name = event["image_name"]
    cluster_arn = event["cluster_arn"]
    
    # Pull the Docker image from the specified repository
    ecs_client.pull_image(
        repositoryName=image_name,
        imageTag="latest"
    )
    
    # Load the container onto the cluster, but do not start it
    ecs_client.register_task_definition(
        family=container_name,
        containerDefinitions=[
            {
                "name": container_name,
                "image": image_name,
                "cpu": 1024,
                "memory": 4096,
                "essential": False
            }
        ]
    )

