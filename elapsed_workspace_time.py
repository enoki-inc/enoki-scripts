#lambda function for returning the elapsed time a workspace has been active

import datetime

def lambda_handler(event, context):
    # Extract the current time
    now = datetime.datetime.now()
    
    # Extract the timestamp of the previous function execution from the event data
    previous_function_timestamp = event["previous_function_timestamp"]
    
    # Convert the timestamp to a datetime object
    previous_function_time = datetime.datetime.fromtimestamp(previous_function_timestamp)
    
    # Calculate the difference between the current time and the previous function execution time
    elapsed_time = now - previous_function_time
    
    # Calculate the number of hours, minutes, and seconds separately
    hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Format the elapsed time as a string in the format "X hours Y minutes Z seconds"
    elapsed_time_str = f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"
    
    # Return the elapsed time string
    return elapsed_time_str

