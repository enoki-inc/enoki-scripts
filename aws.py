import os
import subprocess

def main():
    # Check if isAWS environment variable is set to True
    if os.environ.get('isAWS') != 'True':
        print("isAWS environment variable is not set to True")
        return

    # Get the AWS access key ID and secret access key from environment variables
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    if aws_access_key_id is None or aws_secret_access_key is None:
        print("AWS_ACCESS_KEY_ID and/or AWS_SECRET_ACCESS_KEY environment variables are not set")
        return

    # Automatically log in to AWS
    print("Logging in to AWS with credentials...")
    process = subprocess.run(['aws', 'configure', 'set', 'aws_access_key_id', aws_access_key_id], capture_output=True)
    process = subprocess.run(['aws', 'configure', 'set', 'aws_secret_access_key', aws_secret_access_key], capture_output=True)

    # Get the AWS repo link from the environment variable
    repo_link = os.environ.get('AWS_REPO_LINK')
    if repo_link is None:
        print("AWS_REPO_LINK environment variable is not set")
        return

    # Clone the repository
    print("Cloning repository...")
    process = subprocess.run(['git', 'clone', repo_link], capture_output=True)

    # Open the repository in Visual Studio Code
    print("Opening repository in Visual Studio Code...")
    process = subprocess.run(['code', '.'], cwd=os.path.basename(repo_link.rstrip('.git')), capture_output=True)

if __name__ == '__main__':
    main()

