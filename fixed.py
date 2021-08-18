import subprocess
print(str(subprocess.check_output(['ls'],shell=True)))