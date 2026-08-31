# Steps

1. Install VS CODE
https://code.visualstudio.com/download?_exp_download=fb315fc982

2. Create a new folder
  2.1 Click that folder
  2.2 Click on address bar and write cmd
  2.3 A terminal(CLI) will appear
  2.4 write code . and press enter

3. Install Python
https://www.python.org/downloads/
 3.1 Verify python by running a command: 
 
4. UV Package manager
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  Note: Restart your terminal window after installation finishes so the system can locate the uv command.

    4.1 Verify UV package manager by command: 
    uv 0.12.7 (61291a8ca 2026-08-27 x86_64-pc-windows-msvc)



# Getting started with FASTAPI Installation
1. Run command: uv venv
2. Run command: .venv\Scripts\activate
3. Run command to install packages: uv pip install fastapi uvicorn
4. uv init
5. make a new file name `main.py`

# Homework
1. Do all the installations with hello world code
2. Run the fastapi application. Find out the command