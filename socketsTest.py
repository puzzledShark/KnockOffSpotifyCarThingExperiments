import socket
import time

def main():
    # Define the recipient's address and port
    recipient_address = '127.0.0.1'  # localhost
    recipient_port = 12345

    # Create a UDP socket
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send numbers from 1 to 100
#

    commands = [
        "Play",
        "Next",
        "Previous",
        "VolumeUp",
        "VolumeDown",
        "1"
    ]

    for command in commands:
        sender_socket.sendto(command.encode(), (recipient_address, recipient_port))
        print("Sent:", command)
        time.sleep(3)

    # Close the socket
    sender_socket.close()

if __name__ == "__main__":
    main()
