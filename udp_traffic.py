import socket
import random
import time

TARGET = "127.0.0.1"
PORT = 9999
PACKET_SIZE = 1024
DELAY = 0.005   # control speed

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Starting UDP traffic generator...")

try:
    while True:
        data = random._urandom(PACKET_SIZE)
        sock.sendto(data, (TARGET, PORT))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("\nStopped by user")