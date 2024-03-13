######################################### PACKAGES ##############################################################
from subprocess import check_call, call, CalledProcessError
from os.path import exists
from os import chdir
from sys import executable, modules
from pkg_resources import require, DistributionNotFound, VersionConflict


######################################### METHODS ##########################################################################


# Activate the virtual environment
def call_activate():
    try:
        call('activate.bat', shell=True)
        print('Virtual environment activated (only affects this subprocess)\n')
    except Exception as e:
        print(f'Error to activate the virtual environment: {e}\n')


# creates and activates the virtual environment venv
def manage_and_activate_env():
    venv_path = 'venv/Scripts'
    if exists(venv_path):
        chdir(venv_path)
        call_activate()
        chdir('../../')
    else:
        print(f"The package {venv_path} doesn't exist.\nInstalling venv...\n")
        call([executable, '-m', 'venv', 'venv'])
        if exists(venv_path):
            chdir(venv_path)
            call_activate()
            chdir('../../')


# Function to install a package
def check_and_install_package(package):
    try:
        require(package)
        print(f'\nPackage already installed.\n')
    except DistributionNotFound:
        print(f"\nThe package {package} doesn't exist.\nInstalling package...\n")
        check_call([executable, '-m', 'pip', 'install', package])
    except VersionConflict as vc:
        installed_version = vc.dist.version
        required_version = vc.req
        print(f"\nA version's conflict detected:\n"
              f"Version installed: {installed_version}"
              f"Version required: {required_version}"
               "Trying to install the package required\n")
        check_call([executable, '-m', 'pip', 'install', '--upgrade', package])
    except CalledProcessError as cp:
        print(f"\nAn error has occurred: {cp.returncode}\n")
        check_call(([executable, '-m', 'pip', 'install', '--upgrade', package]))
        check_call([executable, '-m', 'pip', 'install', package])



# Function to install all packages written in requirements.txt
def check_and_install_packages(file, STANDARD_PACKAGE):
    with open(file, 'r') as packages:
        for package in packages.readlines():
            if package.strip() in STANDARD_PACKAGE:
                print(f"Package {package.strip()} already installed!\n")
            else:
                check_and_install_package(package.strip())

    packages.close()

def run():
    STANDARD_PACKAGE = []

    manage_and_activate_env()
    for key in modules.keys():
        STANDARD_PACKAGE.append(key.strip())


    while True:
        selection = input('1. Install an only package\n'
                          '2. Install all packages written to the requirements.txt type file\n'
                          '(Other). Exit\n'
                          'Enter the option: ')

        if selection == '1':
            package = input('Enter the package which you want to install: ')
            if package in STANDARD_PACKAGE:
                print('Package already installed!\n')
            else:
                check_and_install_package(package)
        elif selection == '2':
            file = input('Enter your file with the packages to install (requirements.txt): ')
            check_and_install_packages(file, STANDARD_PACKAGE)
        else:
            print('************************* VIRTUALVENV CONFIGURATION FINISHED *******************************************************\n')
            break


"""
######################################### PACKAGES ##############################################################
from subprocess import check_call, call, CalledProcessError
from os.path import exists
from os import chdir
from sys import executable, modules
from pkg_resources import require, DistributionNotFound, VersionConflict


######################################### METHODS ##########################################################################


# Activate the virtual environment
def call_activate():
    try:
        call('activate.bat', shell=True)
        print('Entorno virtual activado.\n')
    except Exception as e:
        print(f'Error al activar el entorno virtual: {e}\n')


# creates and activates the virtual environment venv
def manage_and_activate_env():
    venv_path = 'venv/Scripts'
    if exists(venv_path):
        chdir(venv_path)
        call_activate()
        chdir('../../')
    else:
        print(f"El paquete {venv_path} no existe.\nInstalando venv...\n")
        call([executable, '-m', 'venv', 'venv'])
        if exists(venv_path):
            chdir(venv_path)
            call_activate()
            chdir('../../')


# Function to install a package
def check_and_install_package(package):
    try:
        require(package)
        print(f'\nPaquete ya instalado\n')
    except DistributionNotFound:
        print(f"\nEl paquete {package} no existe.\nInstalando paquete...\n")
        check_call([executable, '-m', 'pip', 'install', package])
    except VersionConflict as vc:
        installed_version = vc.dist.version
        required_version = vc.req
        print(f"\nDetectado un conflicto de versiones:\n"
              f"Versión instalada: {installed_version}"
              f"Versión requerida: {required_version}"
               "Intentando instalar el paquete requerido\n")
        check_call([executable, '-m', 'pip', 'install', '--upgrade', package])
    except CalledProcessError as cp:
        print(f"\nHa ocurrido un error: {cp.returncode}\n")
        check_call(([executable, '-m', 'pip', 'install', '--upgrade', package]))
        check_call([executable, '-m', 'pip', 'install', package])



# Function to install all packages written in requirements.txt
def check_and_install_packages(file, STANDARD_PACKAGE):
    with open(file, 'r') as packages:
        for package in packages.readlines():
            if package.strip() in STANDARD_PACKAGE:
                print(f"Paquete {package.strip()} ya instalado!\n")
            else:
                check_and_install_package(package.strip())

    packages.close()

def run():
    STANDARD_PACKAGE = []

    manage_and_activate_env()
    for key in modules.keys():
        STANDARD_PACKAGE.append(key.strip())


    while True:
        selection = input('1. Instale un solo paquete\n'
                          '2. Instale todos los paquetes escritos en el archivo tipo requirements.txt\n'
                          '(Otra tecla). Salir\n'
                          'Seleccione una opción: ')

        if selection == '1':
            package = input('Introduzca el paquete que desea instalar: ')
            if package in STANDARD_PACKAGE:
                print('Paquete ya instalado!\n')
            else:
                check_and_install_package(package)
        elif selection == '2':
            file = input('Introduzca su archivo con los paquetes a instalar (requirements.txt): ')
            check_and_install_packages(file, STANDARD_PACKAGE)
        else:
            print('************************* CONFIGURACIÓN VIRTUALENV FINALIZADA *******************************************************\n')
            break

"""


