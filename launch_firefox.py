import subprocess

# Read the urls.txt file and store the URLs in an array
with open("urls.txt", "r") as file:
    urls = file.readlines()

subprocess.run(['firefox'] + urls)
