import psutil
import fcntl

# Get the process of code-server
code_server = None
for proc in psutil.process_iter():
    if proc.name() == "code-server":
        code_server = proc
        break

# Check if code-server is running
if code_server is None:
    print("Error: code-server is not running.")
    exit(1)

# Get a list of the filepaths of the files open in code-server
open_files = code_server.open_files()
filepaths = []
for file_desc in open_files:
    filepath = fcntl.fcntl(file_desc.fd, fcntl.F_GETPATH)
    filepaths.append(filepath)

# Save the filepaths to a file
with open("open_files.txt", "w") as f:
    for filepath in filepaths:
        f.write(filepath + "\n")

print("Filepaths of open files in code-server saved to open_files.txt.")

