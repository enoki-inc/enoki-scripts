#lambda function to create s3 bucket automatically with team's name as name of s3 bucket sourced from postgresql db in aws rds 
import boto3
import psycopg2

def lambda_handler(event, context):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="rds-hostname",
        database="database",
        user="user",
        password="password"
    )
    cursor = conn.cursor()
    
    # Retrieve the team name from the database
    cursor.execute("SELECT name FROM teams WHERE id = %s", (event['team_id'],))
    team_name = cursor.fetchone()[0]
    
    # Close the database connection
    cursor.close()
    conn.close()
    
    # Create an S3 bucket with the team name
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=team_name)
    
    return {
        "team_name": team_name,
        "bucket_name": team_name
    }

