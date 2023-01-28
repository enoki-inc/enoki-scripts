import os
import subprocess
import boto3

def delete_folder(event, context):
    # Create a client for the EFS service
    efs_client = boto3.client('efs')

    # Get the EFS file system ID and folder path from the event
    file_system_id = event['file_system_id']
    folder_path = event['folder_path']

    # Get the DNS name for the EFS file system
    file_system = efs_client.describe_file_systems(FileSystemId=file_system_id)
    dns_name = file_system['FileSystems'][0]['Name']

    # Mount the EFS file system to the local file system
    mount_command = f"mount -t nfs4 -o nfsvers=4.1 {dns_name}:/ {folder_path}"
    subprocess.run(mount_command, shell=True)

    # Delete the folder using the rm command
    delete_command = f"rm -rf {folder_path}/*"
    subprocess.run(delete_command, shell=True)

    # Unmount the EFS file system from the local file system
    unmount_command = f"umount {folder_path}"
    subprocess.run(unmount_command, shell=True)
