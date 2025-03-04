# 🔐 LUKS Key Management (lukyma)

**Lukyma** is a Python tool for managing LUKS encryption keys. It allows you to add a new key with a specified memory cost and securely remove an old key—ideal for devices with limited RAM (e.g., Raspberry Pi).

![GitHub license](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python version](https://img.shields.io/badge/Python-3.x-blue.svg)

## 🎯 Purpose

Lukyma simplifies LUKS key management by offering an interactive interface to add and remove encryption keys efficiently. Its streamlined workflow makes it perfect for maintaining secure systems without manual key juggling.

## 🚀 Features

- **Add New Key:** Insert a new LUKS key with a user-defined memory cost.
- **Remove Old Key:** Securely remove an existing LUKS key.
- **Interactive Device Selection:** Choose the block device to manage from a list.
- **Automated Prompts:** Guided prompts for passphrases and memory cost inputs.

## 🛠 Prerequisites

- **Python 3.x** 🐍
- **cryptsetup** installed on your system 🔧
- **python-pexpect** module (install via pip)

Install the required Python package:
```bash
pip install python-pexpect
```

## 📥 Installation

Clone the repository and set it up:
```bash
git clone https://github.com/your-username/luks-key-management.git
cd luks-key-management
chmod +x main.py
```

You can install this tool using Kevins Package Manager with the alias **lukyma**:
```bash
kevins-package-manager install lukyma
```

## 🚀 Usage

Run the script with superuser privileges:
```bash
sudo python ./main.py
```

### Interactive Steps

1. **Select Device:** The script lists available block devices. Choose the device number you want to manage.
2. **Enter Existing Passphrase:** Provide the current LUKS passphrase when prompted.
3. **Enter New Passphrase:** Input the new passphrase for the key.
4. **Specify Memory Cost:** Enter the memory cost (in Kilobytes) to configure the new key.
5. **Key Management:** The script will add the new key with the specified memory cost and then prompt you to remove the old key.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Developed by **Kevin Veen-Birkenbach**  
- 🌐 [cybermaster.space](https://cybermaster.space/)  
- 📧 [kevin@veen.world](mailto:kevin@veen.world)

## ⚠️ Disclaimer

**Lukyma** was developed for educational and practical purposes. Always back up your data before modifying your LUKS configuration. Use this tool at your own risk.

---

Feel free to contribute, report issues, or suggest improvements!
