import socket
import time
import sys

def send_message(message, host='192.168.1.13', port=9002):
    """
    Send a message to the specified host and port
    """
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to the server
            sock.connect((host, port))
            
            # Send the message (encode to bytes)
            sock.sendall(message.encode('utf-8'))
            
            print(f"Message sent successfully: {message}")
            return True
            
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

def main():
    # Messages to send in rotation
    messages = [
        "Ahmed is unknown person",
    ]
    
    message_index = 0
    send_interval = 2  # seconds between messages
    
    print("Starting message sender...")
    print("Sending messages to 192.168.1.14:9002")
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            # Get current message
            current_message = messages[message_index]
            
            # Send the message
            send_message(current_message)
            
            # Move to next message (cycle through the list)
            message_index = (message_index + 1) % len(messages)
            
            # Wait before sending next message
            time.sleep(send_interval)
            
    except KeyboardInterrupt:
        print("\n\nStopping message sender...")
        sys.exit(0)

if __name__ == "__main__":
    main()

######################################################

# import socket
# import time
# import sys
# import threading

# def send_to_port(message, host, port, port_name):
#     """
#     Send a message to a specific port
#     """
#     try:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#             sock.settimeout(5)  # 5 second timeout
#             sock.connect((host, port))
#             sock.sendall(message.encode('utf-8'))
#             print(f"✓ Message sent to {port_name} (Port {port}): {message}")
#             return True
#     except Exception as e:
#         print(f"✗ Error sending to {port_name} (Port {port}): {e}")
#         return False

# def send_message_both_ports(message, host='192.168.1.14', ports=[9002, 9003]):
#     """
#     Send message to both ports simultaneously using threads
#     """
#     threads = []
#     results = []
    
#     # Create threads for each port
#     for port in ports:
#         port_name = f"Port_{port}"
#         thread = threading.Thread(
#             target=lambda p=port, name=port_name: results.append(
#                 send_to_port(message, host, p, name)
#             )
#         )
#         threads.append(thread)
    
#     # Start all threads
#     for thread in threads:
#         thread.start()
    
#     # Wait for all threads to complete
#     for thread in threads:
#         thread.join()
    
#     return all(results)

# def main():
#     # Configuration
#     host = '192.168.1.11'
#     ports = [9002, 9002]  # Add more ports if needed
    
#     messages = [
#         "Youssef is known person",
#         "Mohanned is known person"
#     ]
    
#     message_index = 0
#     send_interval = 2  # seconds between message cycles
    
#     print("Starting multi-port message sender...")
#     print(f"Sending to: {host}:{ports}")
#     print("Press Ctrl+C to stop\n")
    
#     try:
#         while True:
#             current_message = messages[message_index]
            
#             print(f"\n[{time.strftime('%H:%M:%S')}] Sending: '{current_message}'")
#             print("-" * 50)
            
#             # Send to both ports simultaneously
#             success = send_message_both_ports(current_message, host, ports)
            
#             if success:
#                 print(f"✓ All messages delivered successfully!")
#             else:
#                 print("⚠ Some messages failed to deliver")
            
#             # Move to next message
#             message_index = (message_index + 1) % len(messages)
            
#             # Wait before next cycle
#             time.sleep(send_interval)
            
#     except KeyboardInterrupt:
#         print("\n\nStopping multi-port message sender...")
#         sys.exit(0)

# if __name__ == "__main__":
#     main()