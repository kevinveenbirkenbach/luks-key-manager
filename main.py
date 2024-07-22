import pexpect

def run_command(command, passphrase=None, new_passphrase=None, mem_cost=None):
    print(f"Executing: {' '.join(command)}")
    child = pexpect.spawn(' '.join(command), encoding='utf-8')

    if passphrase:
        child.expect('Enter any existing passphrase: ')
        child.sendline(passphrase)

    if mem_cost:
        child.expect('Enter new passphrase for key slot: ')
        child.sendline(new_passphrase)
        child.expect('Verify passphrase: ')
        child.sendline(new_passphrase)

    child.expect(pexpect.EOF)
    output = child.before
    print(f"Output:\n{output}")
    return child

def get_block_devices():
    devices = []
    result = run_command(['lsblk', '-pno', 'NAME'])
    devices = [line.strip() for line in result.before.split('\n') if line.strip()]
    devices = [device.replace('|-', '').replace('├─', '').replace('└─', '').replace('`-', '').strip() for device in devices]
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
        cost = input("Enter memory cost in Kilobyte(KB): ")
        if cost.isdigit() and int(cost) > 0:
            return cost
        else:
            print("Invalid input. Please enter a positive number.")

def add_key(device, existing_passphrase, new_passphrase, mem_cost):
    command = ['sudo', 'cryptsetup', 'luksAddKey', '--pbkdf-memory', str(mem_cost), device]
    result = run_command(command, passphrase=existing_passphrase, new_passphrase=new_passphrase, mem_cost=mem_cost)
    return result.exitstatus == 0

def remove_key(device):
    old_passphrase = get_passphrase("Enter the old passphrase to remove the old key: ")
    command = ['sudo', 'cryptsetup', 'luksRemoveKey', device]
    result = run_command(command, passphrase=old_passphrase)
    if result.exitstatus == 0:
        print("Old key removed successfully.")
    else:
        print("Failed to remove the old key.")

def main():
    devices = get_block_devices()
    if not devices:
        print("No block devices found.")
        return

    device = choose_device(devices)
    existing_passphrase = get_passphrase("Enter the existing passphrase: ")
    new_passphrase = get_passphrase("Enter the new passphrase: ")
    mem_cost = get_memory_cost()

    if add_key(device, existing_passphrase, new_passphrase, mem_cost):
        remove_key(device)
    else:
        print("Failed to add new key.")

if __name__ == "__main__":
    main()
