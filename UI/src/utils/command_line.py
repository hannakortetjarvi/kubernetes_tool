import subprocess
from PySide6.QtWidgets import QApplication

def command_call(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Print the output of the command
        return True, f"Output:\n{result.stdout}"
    else:
        # Print the error message if the command failed
        return False, f"Output:\n{result.stderr}"
    
def multiple_line_command_call(command, browser):
    browser.setText("")
    cmds = command.split(" ")
    result = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    app = QApplication.instance()

    # Check if the command was successful
    for line in result.stdout:
        # Print the output line
        print(line.decode())
        
        # Update the browser with the output line
        browser.append(str(line))
        app.processEvents()