# 💻 Python-Based Smart Laptop Automation Assistant

A Python-based Smart Laptop Automation Assistant designed to simplify everyday laptop operations through simple text commands and automated voice responses.

This project uses Python libraries to interact with Windows system utilities, hardware components, applications, and web browsers.

## 🚀 Project Overview

The Smart Laptop Automation Assistant allows users to perform common laptop operations without manually navigating through multiple system settings or applications.

Users can enter commands, and the assistant processes them to perform the requested task and provides spoken responses using Windows Speech API (SAPI).

## ✨ Key Features

### 1. System Monitoring
- Check battery percentage and charging status.
- Monitor RAM usage.
- Check CPU utilization.
- View available C drive storage.
- Retrieve operating system information.

### 2. Date and Time
- Display current time.
- Display today's date.
- Identify the current day.

### 3. Application Automation
- Open Notepad.
- Open Calculator.
- Launch Microsoft Excel.
- Launch Microsoft Power BI.
- Open Google and YouTube.
- Open Gmail.

### 4. Hardware Control
- Check Bluetooth status.
- Turn Bluetooth ON/OFF.
- Check current screen brightness.
- Increase or decrease screen brightness.

### 5. Camera Access
- Access the laptop webcam using OpenCV.
- Display live camera footage.
- Press `Q` to close the camera window.

### 6. Internet Connectivity
- Check whether an internet connection is available.

### 7. Voice Response
- Convert assistant responses into speech using Windows SAPI.
- Display responses in the terminal.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OS | Application launching and system operations |
| Sys | Python system utilities |
| Platform | Operating system information |
| Socket | Internet connectivity checking |
| Datetime | Date and time information |
| Webbrowser | Opening websites |
| PyWin32 | Windows Speech API integration |
| PSUtil | System monitoring |
| Screen Brightness Control | Display brightness management |
| WinRT | Bluetooth hardware control |
| OpenCV | Webcam access and live video |

## 📂 Project Structure

```text
Python-Laptop-Automation-Assistant/
│
├── laptop_assistant.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/Python-Laptop-Automation-Assistant.git
```

**Step 2: Navigate to the project folder**

```bash
cd Python-Laptop-Automation-Assistant
```

**Step 3: Create a virtual environment**

```bash
python -m venv .venv
```

**Step 4: Activate the environment (Windows)**

```powershell
.venv\Scripts\activate
```

**Step 5: Install the required dependencies**

```bash
pip install pywin32 psutil screen-brightness-control opencv-python winsdk
```

Install and verify the WinRT Bluetooth dependency separately if your Python environment requires a different Windows SDK package.

**Step 6: Run the project**

```bash
python laptop_assistant.py
```

## 💡 Example Commands

```text
Check battery percentage
What is the current time?
Check RAM usage
What is my CPU usage?
Check C drive storage
Open Notepad
Open Calculator
Open YouTube
Open Google
Check internet connection
Turn on Bluetooth
Turn off Bluetooth
Increase brightness
Decrease brightness
Open Camera
Open Excel
Open Power BI
Open Gmail
```

## 🎯 Project Objectives

- Understand Python-based system automation.
- Work with operating system utilities.
- Explore hardware interaction using Python.
- Implement system resource monitoring.
- Integrate text-to-speech functionality.
- Develop practical problem-solving skills.

## 🔮 Future Enhancements

- Speech-to-text command recognition.
- AI-powered natural language command processing.
- More application automation.
- Improved error handling and hardware compatibility.
- Additional system management features.

## 👩‍💻 Developer

Developed as a hands-on Python automation project to explore system programming, hardware interaction, and real-world Python applications.

**If you find this project useful, consider giving the repository a ⭐!**