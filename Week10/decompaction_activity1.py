import datetime

def log_event(event_type, user_id, message):

    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create formatted log message
    log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"
    
    # Write log message to file
    with open("rental_log.txt", "a") as log_file:
        log_file.write(log_message)

# Example usage:
log_event("INFO", "Bhagya-User", "User logged in.")
log_event("ERROR", "Bhagya-User", "Failed to book a car")
