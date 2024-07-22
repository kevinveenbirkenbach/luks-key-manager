# 🔐 LUKS Key Management Script

This repository contains a Python script for managing LUKS encryption keys. The script allows you to add a new key with specified memory cost and remove an old key securely. This is particularly useful for systems with limited RAM, such as Raspberry Pi.

## 🎯 Purpose

The purpose of this script is to simplify the management of LUKS encryption keys by providing an interactive tool that can be used to add and remove keys efficiently. This script was inspired by a discussion on the Debian forums: [Debian Forum Discussion](https://forums.debian.net/viewtopic.php?t=159242).

## 🚀 Usage

### Prerequisites

- Python 3.x 🐍
- `cryptsetup` installed on your system 🔧

### Running the Script

1. Clone the repository:
   ```bash
   git clone https://github.com/kevinveenbirkenbach/luks-key-management-script.git
   cd luks-key-management-script
   ```

2. Make the script executable:
   ```bash
   chmod +x main.py
   ```

3. Run the script:
   ```bash
   sudo ./main.py
   ```

### Interactive Steps

1. **Select Device:** The script will list available block devices. Choose the device you want to manage.
2. **Enter New Passphrase:** You will be prompted to enter a new passphrase.
3. **Enter Memory Cost:** Specify the memory cost in MiB. The script will convert this to bytes.
4. **Add and Remove Key:** The script will add a new key with the specified memory cost and then prompt you to enter the old passphrase to remove the old key.

## 📜 License

This project is licensed under the GNU Affero General Public License v3.0. For more details, see the [LICENSE](LICENSE) file.

## 👨‍💻 Author

This script was programmed by Kevin Veen-Birkenbach. For more information, visit [Kevin's Website](https://cybermaster.space/) 🌐 or contact him at [kevin@veen.world](mailto:kevin@veen.world) 📧.

## ⚠️ Note

This repository and script were generated with the help of AI 🤖 and are intended for educational and practical purposes. Use at your own risk and ensure you have backups of your data before making any changes to your LUKS setup. Checkout the conversation with [ChatGPT](https://chatgpt.com/share/740700df-9391-4b74-9d60-51b786cd0452).
