#--coding: utf-8 --

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
    cmds = command.split(" ")
    result = ""
    try:
        result = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        return "Command does not exist."
    app = QApplication.instance()

    for line in result.stdout:
        # Print the output line
        print(line.decode('utf-8').rstrip('\r|\n'))
        
        # Update the browser with the output line
        browser.append(str(line.decode('utf-8').rstrip('\r|\n')))
        app.processEvents()

    return result.returncode