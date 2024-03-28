import subprocess

def command_call(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Print the output of the command
        return True, f"Output:\n{result.stdout}"
    else:
        # Print the error message if the command failed
        return False, f"Output:\n{result.stderr}"