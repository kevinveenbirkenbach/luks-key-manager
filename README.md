# 🔐 LUKS Key Manager (lukyma)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


**LUKS Key Manager** is a Python tool for managing LUKS encryption keys. It allows you to add a new key with a specified memory cost and securely remove an old key—ideal for devices with limited RAM (e.g., Raspberry Pi). This tool is supported by the **lukyma** alias through Kevin's Package Manager.

![GitHub license](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python version](https://img.shields.io/badge/Python-3.x-blue.svg)

## 🎯 Purpose

LUKS Key Manager simplifies the management of LUKS encryption keys by offering an interactive interface to add and remove keys efficiently. Its streamlined workflow makes it perfect for maintaining secure systems without the hassle of manual key juggling.

## 🚀 Features

- **Add New Key:** Insert a new LUKS key with a user-defined memory cost.
- **Remove Old Key:** Securely remove an existing LUKS key.
- **Interactive Device Selection:** Choose the block device to manage from a dynamically generated list.
- **Automated Prompts:** Guided prompts for entering passphrases and memory cost values.

## 🛠 Prerequisites

- **Python 3.x** 🐍
- **cryptsetup** installed on your system 🔧
- **python-pexpect** module (install via pip)

Install the required Python package:
```bash
pip install python-pexpect
```

## 📥 Installation

You can install **LUKS Key Manager** easily using [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager). Once you have the package manager set up, simply run:

```bash
pkgman install lukyma
```

This command installs the tool under the alias **lukyma**, which serves as the support framework for **LUKS Key Manager**.

## 🚀 Usage

Run the script with superuser privileges:
```bash
sudo lukyma ./main.py
```

### Interactive Steps

1. **Select Device:** The tool lists available block devices—choose the device number you wish to manage.
2. **Enter Existing Passphrase:** Provide the current LUKS passphrase when prompted.
3. **Enter New Passphrase:** Input the new passphrase for the key.
4. **Specify Memory Cost:** Enter the memory cost (in Kilobytes) to configure the new key.
5. **Key Management:** The script will add the new key with the specified memory cost, then prompt you to remove the old key.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Developed by **Kevin Veen-Birkenbach**  
- 🌐 [cybermaster.space](https://cybermaster.space/)  
- 📧 [kevin@veen.world](mailto:kevin@veen.world)

## ⚠️ Disclaimer

**LUKS Key Manager** is provided for educational and practical purposes. Always back up your data before making changes to your LUKS configuration. Use this tool at your own risk.

---

Feel free to contribute, report issues, or suggest improvements!
