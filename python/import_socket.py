import socket
import threading

# Function to handle commands sent to each device
def device_listener(device_id, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(1)
    print(f"Device {device_id} listening on port {port}...")

    while True:
        client_socket, address = server_socket.accept()
        command = client_socket.recv(1024).decode()
        print(f"Device {device_id} received command: {command}")
        client_socket.send(f"Device {device_id} executed command: {command}".encode())
        client_socket.close()

# Function to send commands to all devices
def send_command_to_devices(command, ports):
    for port in ports:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", port))
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print(response)
        client_socket.close()

# Start listeners for 10 devices (for demonstration purposes)
ports = [5000 + i for i in range(10)]
threads = []
for i, port in enumerate(ports):
    thread = threading.Thread(target=device_listener, args=(i + 1, port))
    threads.append(thread)
    thread.start()

# Send a command to all devices
send_command_to_devices("Perform stock trade", ports)