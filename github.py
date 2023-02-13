import os
import subprocess

def main():
    # Check if isGithub environment variable is set to True
    if os.environ.get('isGithub') != 'True':
        print("isGithub environment variable is not set to True")
        return

    # Get the github token from environment variables
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token is None:
        print("GITHUB_TOKEN environment variable is not set")
        return

    # Automatically log in to GitHub
    print("Logging in to GitHub with token...")
    process = subprocess.run(['git', 'config', '--global', 'user.name', '"GitHub Actions"'], capture_output=True)
    process = subprocess.run(['git', 'config', '--global', 'user.email', '"github-actions@users.noreply.github.com"'], capture_output=True)
    process = subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], capture_output=True)
    process = subprocess.run(['echo', f'https://{github_token}:x-oauth-basic@github.com'], capture_output=True, text=True, input=github_token, encoding='ascii')

    # Get the GitHub repo link from the environment variable
    repo_link = os.environ.get('GITHUB_REPO_LINK')
    if repo_link is None:
        print("GITHUB_REPO_LINK environment variable is not set")
        return

    # Clone the repository
    print("Cloning repository...")
    process = subprocess.run(['git', 'clone', repo_link], capture_output=True)

    # Open the repository in Visual Studio Code
    print("Opening repository in Visual Studio Code...")
    process = subprocess.run(['code', '.'], cwd=os.path.basename(repo_link.rstrip('.git')), capture_output=True)

if __name__ == '__main__':
    main()

