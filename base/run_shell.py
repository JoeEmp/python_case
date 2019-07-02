import os
import subprocess
import time
import sys

if __name__ == "__main__":
    result = os.system('cd ~/Documents/github')
    # print(result)
    popen = os.popen('ls')
    # print(popen.read())

    sub_result = subprocess.call(['cd','~/'])
    print(sub_result)
    sub_popen = subprocess.Popen('ls',stdout=subprocess.PIPE)
    print(sub_popen.communicate())
    print(sub_popen.returncode)