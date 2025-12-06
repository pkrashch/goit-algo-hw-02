import queue
import time
import random

# Create the request queue
request_queue = queue.Queue()
request_counter = 0

def generate_request():
    """
    Creates a new request with a unique ID and adds it to the queue.
    """
    global request_counter
    request_counter += 1

    request = {
        "id": request_counter,
        "description": f"Request #{request_counter} for service"
    }
    # Add the request to the queue
    request_queue.put(request)
    print(f"Generated and added to queue: {request['description']}")

def process_request():
    """
    Removes a request from the queue and simulates its processing.
    """
    # Check if the queue is not empty
    if not request_queue.empty():
        # Remove the request from the queue
        request_to_process = request_queue.get()
        
        # Simulate processing
        print(f"Processing: {request_to_process['description']}...")
        
        #Simulating processing time
        time.sleep(0.5) 
        
        print(f"Processing finished: Request ID {request_to_process['id']}")
    else:
        # Print a message that the queue is empty
        print("⏸Queue is empty. Waiting for new requests...")

# --- Main Program Loop ---
def main_loop():
    print("--- Service Center Simulator (Request Queue) ---")
    
    # Simulate continuous operation
    try:
        while True:
            # Execute generate_request() to create new requests
            generate_request()
            
            # Add a small random delay between generations
            time.sleep(random.uniform(0.1, 0.5))

            # Execute process_request() to handle requests
            process_request()
            
            # Add a pause to make the process visible
            time.sleep(1) 
            
    except KeyboardInterrupt:
        # Handle Ctrl+C press to exit
        print("\n--- Simulator stopped by user. Remaining in queue: ---")
        while not request_queue.empty():
            remaining_request = request_queue.get()
            print(f"- Unprocessed: {remaining_request['description']}")
        print("--- Program finished. ---")

if __name__ == "__main__":
    main_loop()