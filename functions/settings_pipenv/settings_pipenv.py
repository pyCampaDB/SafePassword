from subprocess import check_call, CalledProcessError, run as runSubprocess, check_output
from os.path import exists
from os import  getcwd
from pkg_resources import  VersionConflict, DistributionNotFound



def ensure_pipenv_installed():
    try:
        check_call(['pipenv', '--version'])
        print('pipenv is installed\n')
    except CalledProcessError:
        print('pipenv not found. Install pipenv...')
        check_call(['pip', 'install', 'pipenv'])

def manage_and_use_env():
    if not exists('Pipfile'):
        print('Pipfile not exist. Initializing pipenv environment...\n')
        check_call(['pipenv', 'install'])
    else:

        print('Pipfile exists. Environment ready.\n')


def check_package_installed(package):
    try:
        check_output(['pipenv', 'run', 'pip', 'show', package])
        return True
    except CalledProcessError:
        return False

#Function to install a single package using pipenv
def install_package_with_pipenv(package):
    b = check_package_installed(package)
    if b:
        print(f'\n{package} already installed\n')
    else:
        print(f'\nInstalling {package}...') 
        try:
            runSubprocess(f'pipenv install {package}', shell=True, check=True)
            print(f'\n{package} was installed successfully\n')
        except DistributionNotFound:
            print(f"\nThe package {package} doesn't exist.\nInstalling package...\n")
            runSubprocess(f'pipenv install {package}', shell=True, check=True)
        except VersionConflict as vc:
            installed_version = vc.dist.version
            required_version = vc.req
            print(f"\nA version's conflict detected:\n"
                f"Version installed: {installed_version}"
                f"Version required: {required_version}"
                "Trying to install the package required\n")
            runSubprocess(f'pipenv install --upgrade {package}', shell=True, check=True)
        except CalledProcessError as cp:
            print(f"\nAn error occurred: {cp.returncode}\n")

#Function to install all packages from a requirements.txt file using pipveng
def install_packages_from_file_with_pipenv():
    if exists('requirements.txt'):
        req = 'requirements.txt'
    else:
        req = input('Enter the name file: ')
    
    with open (f'{getcwd()}\\{req}', 'r') as myFile:
        for package in myFile.readlines():
            install_package_with_pipenv(package.strip())

        myFile.close()
    

def uninstall_package():
    package = input('Enter the package name: ')
    try:
        runSubprocess(f'pipenv uninstall {package}', shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')


def check_packages_installed():
    try:
        runSubprocess('pipenv graph', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error occurred: {e.returncode}')


def delete_pipenv():
    try:
        runSubprocess('pipenv --rm', shell=True, check=True)
        runSubprocess('del Pipfile', shell=True, check=True)
        runSubprocess('del Pipfile.lock', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error occurred: {e.returncode}')

def pipenv_run():
    opt = input('pipenv run [your command]. [your command] = ')

    try:
        runSubprocess(f'pipenv run {opt}', shell=True, check=True)
    except CalledProcessError as e:
        print(f'An error occurred: {e.returncode}')


def manage_pipenv():
    menu = '1'
    while menu in ['1', '2', '3', '4', '5', '6']:

        menu = input('\n*********************************** PIPENV SETTINGS ***********************************\n\n'
                             '\n1. Install an only package'
                             '\n2. Install all packages written in requirements.txt'
                             '\n3. Check your packages already installed'
                             '\n4. Uninstall a package'
                             '\n5. Restart your virtual environment'
                             '\n6. Execute your pipenv command'
                             '\n7. Delete the virtual environment'
                             '\n(Other). Exit\n'
                             '\nEnter your choice: ')
                
        if menu=='1':
            package = input('\nEnter package name: ')
            install_package_with_pipenv(package)
        elif menu=='2':install_packages_from_file_with_pipenv()
        elif menu=='3':check_packages_installed()
        elif menu=='4':uninstall_package()
        elif menu=='5':
            delete_pipenv()
            manage_and_use_env()
        elif menu=='6': pipenv_run()
        elif menu=='7': delete_pipenv()
        else: print('\n***************************************** EXIT PIPENV SETTINGS *****************************************\n')
        