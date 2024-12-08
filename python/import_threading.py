import threading

# Function to handle commands on each device
def handle_device(device_id, command):
    print(f"Device {device_id} executing command: {command}")

# Function to send commands to all devices
def send_command_to_all(devices, command):
    threads = []
    for device_id in devices:
        thread = threading.Thread(target=handle_device, args=(device_id, command))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Simulate 1,000 devices
devices = [f"Device_{i}" for i in range(1, 1001)]

# Send a command to all devices
send_command_to_all(devices, "Perform stock trade")