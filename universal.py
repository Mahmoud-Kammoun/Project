import subprocess
from add import getname,getCL
def universalCL (cl):
    #n=str(name)+".py"
    zz=open('fixed.py','w')
    zz.write("import subprocess"+"\n")
    zz.write("print(str(subprocess.check_output(["+"'"+cl+"'"+"],shell=True)))")
    return()

#universalCL("ls")
