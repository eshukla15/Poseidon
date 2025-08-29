# 🖥️  Poseidon - Lil bro of Zeus(Keylogger)
(Educational Purpose Only)

## 📌 Overview
This is a simple **keylogger** script built in Python for **educational and research purposes**.  
It captures keystrokes and logs them into a file for later review, helping me understand how monitoring tools and cybersecurity threats work.  

## ⚠️ Disclaimer
> ⚠️ This software is strictly for **educational use only**.  
> Do not use it for malicious purposes such as spying or stealing sensitive information.  
> Unauthorized use may violate privacy laws and result in legal consequences.  

## 🚀 Features
- Records all keystrokes.
- Saves logs into a text file.
- Lightweight and easy to understand.
- Can be extended for research in security/ethical hacking.
- Can run in **background/stealth mode**.

## 🛠️ Requirements
- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/)

Install dependencies:
```bash
pip install pynput
```

## ▶️ Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/keylogger.git
   cd keylogger
   ```
2. Run the script:
   ```bash
   python keylog.py
   ```
3. Keystrokes will be logged in log.txt.

## 🔒 Security Note
Always run such tools in a controlled environment (like a virtual machine).
This project is meant to teach how keyloggers work, so you can learn how to detect and prevent them in real-world systems.

## 🕵️ Running in Background (Stealth Mode)

# Windows
You can run the script silently in the background by:
```bash
pythonw keylogger.py
```
Or, convert it into an .exe:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole keylogger.py
```
This will generate an executable that runs without a console window.

# Linux / Mac
Run the script in the background:
```bash
nohup python3 keylogger.py &
```
