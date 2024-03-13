############################################# IMPORTS #######################################################################
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from VirtualEnv.VirtualEnv import run as virtualEnv


############################################# METHODS #######################################################################
def codified_password(pwd, file, mode='a+'):
    print(
        '*************************************************************************************************************\n')
    print(f'[*] The password is: {pwd}\n')
    with open(f'{file}.txt', mode) as passFile:
        passFile.write(
            '*************************************************************************************************************\n')
        passFile.write(f'[*] The password is: {pwd}\n\n')

        md5_pass = md5(pwd.encode('utf-8')).hexdigest()
        print(f'[*] MD5 password is: {md5_pass}\n')
        passFile.write(f'[*] MD5 password is: {md5_pass}\n\n')

        sha1_pass = sha1(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-1 password is: {sha1_pass}\n')
        passFile.write(f'[*] SHA-1 password is: {sha1_pass}\n\n')

        sha224_pass = sha224(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-224 password is: {sha224_pass}\n')
        passFile.write(f'[*] SHA-224 password is: {sha224_pass}\n\n')

        sha256_pass = sha256(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-256 password is: {sha256_pass}\n')
        passFile.write(f'[*] SHA-256 password is: {sha256_pass}\n\n')

        sha384_pass = sha384(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-384 password is: {sha384_pass}\n')
        passFile.write(f'[*] SHA-384 password is: {sha384_pass}\n\n')

        sha512_pass = sha512(pwd.encode('utf-8')).hexdigest()
        print(f'[*] SHA-512 password is: {sha512_pass}\n')
        passFile.write(f'[*] SHA-512 password is: {sha512_pass}\n\n')

        passFile.close()


def run():
    virtualEnv()
    menu = '1'

    while menu == '1' or menu == '2' or menu == '3':
        menu = input('1. Codified password\n'
                     '2. Codified 100.000 familiar passwords\n'
                     '3. Verify if your password is in familiar passwords\n'
                     '(Other). Exit\n'
                     'Enter your option: ')
        if menu == '1':
            pwd = input('Enter your password: ')
            file = input('Enter the file name: ')
            codified_password(pwd.strip(), file)

        elif menu == '2':
            passwords = open('familiar passwords.txt', 'r')
            file = input('Enter the file name: ')
            for pwd in passwords.readlines():
                codified_password(pwd.strip(), file)

        elif menu == '3':
            passwords = open('familiar passwords.txt', 'r')
            familiar = False
            pwd = input('Enter your password: ')
            for p in passwords.readlines():
                if p.strip() == pwd:
                    familiar = True
                    break
            if familiar:
                print('\nYour password is in familiar passwords\n')
            else:
                print('\nYour password is not in familiar passwords\n')


        else:
            break


############################################## MAIN #######################################################################
if __name__ == '__main__':
    run()



"""
############################################# IMPORTS #######################################################################
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from VirtualEnv.VirtualEnv import run as virtualEnv


############################################# METHODS #######################################################################
def codified_password(pwd, file, mode='a+'):
    print(
        '*************************************************************************************************************\n')
    print(f'[*] La contraseña es: {pwd}\n')
    with open(f'{file}.txt', mode) as passFile:
        passFile.write(
            '*************************************************************************************************************\n')
        passFile.write(f'[*] La contraseña es: {pwd}\n\n')

        md5_pass = md5(pwd.encode('utf-8')).hexdigest()
        print(f'[*] La contraseña en MD5 es: {md5_pass}\n')
        passFile.write(f'[*] La contraseña en MD5 es: {md5_pass}\n\n')

        sha1_pass = sha1(pwd.encode('utf-8')).hexdigest()
        print(f'[*] La contraseña en SHA-1 es: {sha1_pass}\n')
        passFile.write(f'[*] La contraseña en SHA-1 es: {sha1_pass}\n\n')

        sha224_pass = sha224(pwd.encode('utf-8')).hexdigest()
        print(f'[*] La contraseña en SHA-224 es: {sha224_pass}\n')
        passFile.write(f'[*] La contraseña en SHA-224 es: {sha224_pass}\n\n')

        sha256_pass = sha256(pwd.encode('utf-8')).hexdigest()
        print(f'[*] La contraseña en SHA-256 es: {sha256_pass}\n')
        passFile.write(f'[*] La contraseña en SHA-256 es: {sha256_pass}\n\n')

        sha384_pass = sha384(pwd.encode('utf-8')).hexdigest()
        print(f'[*] La contraseña en SHA-384 es: {sha384_pass}\n')
        passFile.write(f'[*] La contraseña en SHA-384 es: {sha384_pass}\n\n')

        sha512_pass = sha512(pwd.encode('utf-8')).hexdigest()
        print(f'[*] La contraseña en SHA-512 es: {sha512_pass}\n')
        passFile.write(f'[*] La contraseña en SHA-512 es: {sha512_pass}\n\n')

        passFile.close()


def run():
    virtualEnv()
    menu = '1'

    while menu == '1' or menu == '2' or menu == '3':
        menu = input('1. Codifique su contraseña\n'
                     '2. Codifique las 100.000 contraseñas familiares\n'
                     '3. Verifique si su contraseña se encuentra entre las 100.000 contraseñas familiares\n'
                     '(Otra tecla). Salir\n'
                     'Introduzca una opción: ')
        if menu == '1':
            pwd = input('Introduzca su contraseña: ')
            file = input('Introduzca el nombre de su archivo: ')
            codified_password(pwd.strip(), file)

        elif menu == '2':
            passwords = open('familiar passwords.txt', 'r')
            file = input('Introduzca el nombre de su archivo: ')
            for pwd in passwords.readlines():
                codified_password(pwd.strip(), file)

        elif menu == '3':
            passwords = open('familiar passwords.txt', 'r')
            familiar = False
            pwd = input('Introduzca su contraseña: ')
            for p in passwords.readlines():
                if p.strip() == pwd:
                    familiar = True
                    break
            if familiar:
                print('\nTu contraseña está en contraseñas familiares\n')
            else:
                print('\nTu contraseña no está en contraseñas familiares\n')


        else:
            break


############################################## MAIN #######################################################################
if __name__ == '__main__':
    run()
"""