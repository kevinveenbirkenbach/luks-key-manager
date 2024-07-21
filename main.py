import os
import subprocess

def get_block_devices():
    devices = []
    result = subprocess.run(['lsblk', '-dpno', 'NAME'], capture_output=True, text=True)
    if result.returncode == 0:
        devices = result.stdout.strip().split('\n')
    return devices

def choose_device(devices):
    print("Available devices:")
    for i, device in enumerate(devices):
        print(f"{i}: {device}")
    while True:
        choice = input("Select device by number: ")
        if choice.isdigit() and 0 <= int(choice) < len(devices):
            return devices[int(choice)]
        else:
            print("Invalid choice. Please enter a valid number.")

def get_passphrase(prompt):
    return input(prompt)

def get_memory_cost():
    while True:
        cost = input("Enter memory cost in MiB (e.g., 1 for 1 MiB): ")
        if cost.isdigit() and int(cost) > 0:
            return int(cost) * 1024 * 1024
        else:
            print("Invalid input. Please enter a positive number.")

def add_key(device, passphrase, mem_cost):
    result = subprocess.run(
        ['sudo', 'cryptsetup', 'luksAddKey', '--pbkdf-memory', str(mem_cost), device],
        input=passphrase,
        text=True,
        capture_output=True
    )
    return result.returncode == 0

def remove_key(device):
    old_passphrase = get_passphrase("Enter the old passphrase to remove the old key: ")
    result = subprocess.run(
        ['sudo', 'cryptsetup', 'luksRemoveKey', device],
        input=old_passphrase,
        text=True,
        capture_output=True
    )
    if result.returncode == 0:
        print("Old key removed successfully.")
    else:
        print("Failed to remove the old key.")

def main():
    devices = get_block_devices()
    if not devices:
        print("No block devices found.")
        return

    device = choose_device(devices)
    new_passphrase = get_passphrase("Enter the new passphrase: ")
    mem_cost = get_memory_cost()

    if add_key(device, new_passphrase, mem_cost):
        remove_key(device)
    else:
        print("Failed to add new key.")

if __name__ == "__main__":
    main()
