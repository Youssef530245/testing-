import socket
import random
import time
from datetime import datetime, timedelta

# Server info
HOST = "192.168.1.5"
PORT = 9001

# Sample names list
names = ["Youssef", "Mohamed", "Hazem", "Shreef", "Mazen", "Omar", "Nada", "Sarah", "Ali", "Nour"]

def random_time():
    # Generate random time during the day
    start = datetime(2025, 1, 1, 6, 0, 0)
    rand_seconds = random.randint(0, 12 * 3600)  # random time within 12 hours
    t = start + timedelta(seconds=rand_seconds)
    return t.strftime("%H:%M:%S")

def generate_random_message():
    tag = random.randint(1000, 9999)
    name = random.choice(names)
    status = random.choice(["IN", "OUT"])
    time_str = random_time()

    return f"TAG:{tag} | NAME:{name} | STATUS:{status} | TIME:{time_str}"

def main():
    while True:
        try:
            msg = generate_random_message()
            print(f"Sending: {msg}")

            # Create socket and send
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(msg.encode())

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(5)  # send every second

if __name__ == "__main__":
    main()
