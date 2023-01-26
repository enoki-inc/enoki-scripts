import boto3

def lambda_handler(event, context):
    # Create a client for the EFS service
    efs_client = boto3.client('efs')
    
    # Get the ID of the EFS file system you want to delete a folder from
    file_system_id = 'your-efs-file-system-id'
    
    # Get the path of the folder you want to delete
    folder_path = '/path/to/folder'
    
    # Use the EFS client to delete the folder
    efs_client.delete_mount_target(FileSystemId=file_system_id, MountTargetId=folder_path)
    print(f'Folder {folder_path} deleted from EFS file system {file_system_id}')

