import socket
import threading
import time

TARGET = "127.0.0.1"
PORT = 8080
THREADS = 30
DELAY = 0.01   # small delay to control load

def tcp_worker(thread_id):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((TARGET, PORT))
            
            message = f"Hello from thread {thread_id}".encode()
            s.sendall(message)
            
            s.close()
            time.sleep(DELAY)
        except Exception as e:
            print(f"[Thread {thread_id}] Error:", e)

def main():
    print("Starting TCP traffic generator...")
    for i in range(THREADS):
        t = threading.Thread(target=tcp_worker, args=(i,))
        t.daemon = True
        t.start()
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()