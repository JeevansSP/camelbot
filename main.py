import subprocess
import os

# Command to create a virtual environment
subprocess.run(["python", "-m", "venv", "venv"])

# Command to activate the virtual environment based on the operating system
if os.name == 'nt':  # For Windows
    activate_cmd = "venv\\Scripts\\activate.bat"
else:  # For macOS/Linux
    activate_cmd = "source venv/bin/activate"

# Running the activate command
subprocess.run(activate_cmd, shell=True)

# Command to install dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Command to run the batch script
subprocess.run(["streamlit", "run", "_Connect.py"])

