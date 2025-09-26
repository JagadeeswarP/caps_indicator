Caps Lock Indicator – Python Utility for Windows

## ❓ Problem
Many laptops do not provide a clear indication when Caps Lock is ON or OFF.  
This can lead to frustration — especially when typing passwords or working in programming environments.

This tool solves that by providing a tiny, customizable pop‑up whenever Caps Lock state changes.

## ✨ Features
- Displays a pop‑up when Caps Lock is toggled (ON/OFF)
- Auto‑hides after 2 seconds
- Runs silently in background using `pythonw`
- Can be set to run at startup
- Lightweight (no heavy dependencies)

Installation
## ⚡ Installation
1. Clone the repository or copy the code

2. Install dependencies :   pip install pywin32

3. Run the script : python caps_indicator.py

4. (Optional) Run silently in background : pythonw caps_indicator.py

or 

You can create a caps.bat file in the same folder as caps_indicator.py.
In NotePad , copy below code and save it.

@echo off

start "" pythonw "C:\path\to\caps_indicator.py"

Then, add that folder path to the Windows Environment Variables. (Select System Variables --> path --> select and create a new path then-->  paste the path  of caps_indicator.py )

Note: To stop it, Go to task manager search for python.exe or python and END TASK.
After saving and close all the windows, open CMD and type:    caps
Press Caps Lock — you will see a silent pop‑up at the top of your screen.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.
