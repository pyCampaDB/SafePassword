from subprocess import CalledProcessError, run as runSubprocess
from os import getenv


def upload_docker():
    username = getenv('DOCKER_USERNAME', default='default_username')
    pwd = getenv('DOCKER_PASSWORD', default='default_password')
    req = ''
    install_req = ''
    opt = input('Do you have a file named requirements.txt? [Y/N]: ')
    if opt in ['Y', 'y']:
        req = 'requirements.txt'
        install_req = 'RUN pipenv install -r requirements.txt'
    try:
        runSubprocess(['pipenv','run','docker', 'login', '--username', username, '--password', pwd], check=True)

        dockerfile_contents = f"""
#Use the official image of Python
FROM python:3.11.0-slim

#Establised your work directory
WORKDIR /app

#Install pipenv
RUN pip install pipenv

#Copy our Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock {req} /app/

#Installing depends in the system
RUN pipenv install --system --deploy

{install_req}

#Copy all the files
COPY . /app

#Expose the port 8888
EXPOSE 8888

ENV NAME PipEnvironment

CMD pipenv run python pipenvDockerGit.py
    """
        image_name = input('Enter the name of your image: ')

        print('\nWriting Dockerfile\n')
        with open('Dockerfile', 'w') as file:
            file.write(dockerfile_contents)
            file.close()
        print('\nBuilding image...\n')
        runSubprocess(f'pipenv run docker build -t {image_name}:latest .', shell=True, check=True)
        print('\nImage built.\n')
        runSubprocess(f'pipenv run docker push {image_name}', shell=True, check=True)
        print('\nImage uploaded to DockerHub.\n')


    except CalledProcessError as cp:
        print(f'CalledProcessError: {cp.returncode}')
    except Exception as e:
        print(f'Exception: {e.__str__}')

def run_container_docker():
    ports = input('ports: ')
    name_container = input('container: ')
    name_img = input('image: ')
    try:
        runSubprocess('pipenv run docker'
                      f' run -p {ports} --name'
                      f' {name_container} {name_img}',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_start():
    container = input('name container: ')
    try:
        runSubprocess('pipenv run docker '
                      f'start {container}', 
                      shell=True, 
                      check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_stop():
    container = input('name container: ')
    try:
        runSubprocess('pipenv run docker stop'
                      f' {container}', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_restart():
    container = input('name container: ')
    try:
        runSubprocess(f'pipenv run docker restart {container}', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_ps():
    try:
        runSubprocess('pipenv run docker ps', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def docker_ps_a():
    try:
        runSubprocess('pipenv run docker ps -a', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def remove_image():
    img = input(
        '\nEnter the ID of the image: '
    )
    try:
        runSubprocess(f'pipenv run docker rmi {img}', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def remove_container():
    container = input('\nEnter the ID of the container: ')
    try:
        runSubprocess(f'pipenv run docker rm {container}', 
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def exec_it():
    container = input('\nEnter the ID of the container: ')
    try:
        runSubprocess(
            f'pipenv run docker exec -it {container} bash',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def show_logs():
    container = input('\nEnter the ID of the container: ')
    try:
        runSubprocess(
            f'pipenv run docker logs {container}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'\nAn error occurred: {cp.returncode}')

def docker_pull():
    option = ''
    while option not in ['1', '2', '3']:
        
        option = input(
            '\nOptions:\n'
            '1. Write only the name of the image\n'
            '2. Include a tag\n'
            '3. Include a digest\n'
            '\n'
            'Enter your choice: '
        )
        if option not in ['1', '2', '3']:
            print('\nInvalid option\n')
    

    img = input('Enter the image name: ')
    if option == '2': 
        tag = input('Enter the tag of the image: ')
        try:
            runSubprocess(
                f'pipenv run docker pull {img}:{tag}',
                shell=True,
                check=True
            )
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')

    elif option == '3':
        digest = input('Enter the digest of the image: ')
        try:
            runSubprocess(
                f'pipenv run docker pull {img}@{digest}',
                shell=True,
                check=True
            )
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')

    else:
        try:
            runSubprocess(
                f'pipenv run docker pull {img}',
                shell=True,
                check=True
            )
        except CalledProcessError as cp:
            print(f'An error occurred: {cp.returncode}')

def docker_inspect():
    cmd = input('Enter your prompt to inspect: ')
    try:
        runSubprocess(
            f'pipenv run docker inspect {cmd}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')




def manage_docker():
    docker_option = '1'
    while docker_option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        docker_option = input('\n******************** DOCKER: ********************\n'
                                          '1. Upload an image to Docker Hub\n'
                                          '2. Run a docker container\n'
                                          '3. Start docker container\n'
                                          '4. Stop docker container\n'
                                          '5. Restart docker contaienr\n'
                                          '6. Show the containers executing\n'
                                          '7. Show all containers\n'
                                          '8. Remove an image\n'
                                          '9. Remove a container\n'
                                          '10. Show the container\'s logs\n'
                                          '11. Access the virtual environment of your container\n'
                                          '(Other) Exit Docker\n\n'
                                          'Enter your choice: ')
        if docker_option == '1':upload_docker()
        elif docker_option == '2': run_container_docker()
        elif docker_option=='3': docker_start()
        elif docker_option=='4': docker_stop()
        elif docker_option=='5': docker_restart()
        elif docker_option=='6': docker_ps()
        elif docker_option=='7': docker_ps_a()
        elif docker_option=='8': remove_image()
        elif docker_option=='9': remove_container()
        elif docker_option=='10': show_logs()
        elif docker_option=='11': exec_it()
        else: print('\n******************** EXIT DOCKER ********************\n')
