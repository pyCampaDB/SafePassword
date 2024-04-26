from subprocess import  CalledProcessError, run as runSubprocess
from os import  getcwd


def run_script():
    try:
        runSubprocess(f'pipenv run python {input("Enter the file name: ")}.py',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')  

def cmd():
    command = input(f'{getcwd()}: ')
    try:
        runSubprocess(command, shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')
    finally:
        return command
    

def manage_cmd():
    print('\n*********************************** CMD ***********************************\n\n')
    try:
        while True:
            a = cmd()
            if a.lower() == 'exit':
                break                 
    except EOFError:
        pass
    finally:
        print('\n*********************************** EXIT CMD ***********************************\n\n')
        
