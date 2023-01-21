import subprocess

# Check if the open_files.txt file exists
if not os.path.isfile("open_files.txt"):
    print("Error: open_files.txt not found.")
    exit(1)

# Read the open_files.txt file and store the file paths in a list
with open("open_files.txt", "r") as file:
    file_paths = file.read().splitlines()

# Start code-server and open the files in the list
subprocess.run(["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none",  *file_paths])

