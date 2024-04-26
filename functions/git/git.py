from subprocess import CalledProcessError, run as runSubprocess
from os import getenv

def upload_github():
    try:
        email = getenv("GITHUB_EMAIL", default='default_email')
        runSubprocess(f'pipenv run git config --global user.email "{email}"',
                      shell=True, check=True)
        print('\nname')
        username = getenv("GITHUB_USERNAME", default='default_username')
        runSubprocess(f'pipenv run git config --global user.name "{username}"',
                      shell=True, check=True)
        runSubprocess('pipenv run git init', shell=True, check=True)
        print('\nInitializing Github & git status\n')
        runSubprocess('pipenv run git status', shell=True, check=True)
        print('\ngit add .\n')
        runSubprocess('pipenv run git add .', shell=True, check=True)
        commit = input('Enter commit message: ')
        runSubprocess(f'pipenv run git commit -m "{commit}"', shell=True, check=True)

        first_upload = ''
        while first_upload not in ['Y', 'y', 'N', 'n']:
            first_upload = input('Enter if it is your first commit [Y/N]: ')
            if first_upload not in ['Y', 'y', 'N', 'n']:
                print('\nInvalid option\n')
        branch = 'main'
        remote = 'origin'
        if first_upload in ['Y', 'y']:
            remote = input('Enter the remote name: ') #Default: origin
            branch = input('Enter your branch: ')
            runSubprocess(f'pipenv run git branch -M {branch}', shell=True, check=True)           
            my_git = input('Enter repository name: ')
            print('\nremote add origin\n')
            runSubprocess(f'pipenv run git remote add {remote} https://github.com/pyCampaDB/{my_git}.git',
                shell=True, check=True, capture_output=True)
        
        pull = input('Do you want to make a pull? [Y/N]: ')
        if pull in ['Y', 'y']:
            print('\npull\n')
            git_pull(remote, branch)
        print('\npush\n')
        runSubprocess(f'pipenv run git push -u {remote} {branch}', 
                      shell=True, check=True)
        print('\nProject uploaded to GitHub\n')
    except CalledProcessError as cp:
        print(f'\nCalledProcessError: {cp.returncode}\n')
    except Exception as e:
        print(f'Exeption: {e.__str__}')

def git_remote_v():
    try:
        runSubprocess(
            'pipenv run git remote -v', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_remove():
    remote = input(
        'Enter the remote name: '
    )
    try:
        runSubprocess(
            f'pipenv run git remote remove {remote}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_clone():
    url = input(
        'Enter the url of the repository: '
    )
    try:
        runSubprocess(
            f'pipenv run git clone {url}',
            shell= True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_push():
    remote = input(
        'Enter the remote name: '
    )
    branch = input(
        'Enter the branch name: '
    )
    try:
        runSubprocess(
            f'pipenv run git push {remote} {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_branch():
    try:
        runSubprocess(
            'pipenv run git branch',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_checkout():
    try:
        branch = input('Enter the branch name: ')
        runSubprocess(
            f'pipenv run git checkout {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_merge():
    try:
        branch = input('Enter the branch name: ')
        runSubprocess(
            f'pipenv run git merge {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')


def git_pull(remote=None, branch=None):
    if remote == None:
        remote = input('Enter the remote name: ')
    if branch == None:
        branch = input('Enter the branch name: ')
    try:
        runSubprocess(
            f'pipenv run git pull {remote} {branch}',
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')


def manage_git():
    git_option = '1'
    while git_option in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        git_option = input(
                        '\n******************** GIT ********************\n\n'
                        '1. Upload your project to GitHub\n'
                        '2. git remote -v\n'
                        '3. git remote remove origin\n'
                        '4. git clone\n'
                        '5. Send local commits to a remote repository\n'
                        '6. git checkout\n'
                        '7. git merge\n'
                        '8. Display the availables local branches of the repository\n'
                        '9. git pull\n'
                        '(Other) Exit GIT\n\n'
                        'Enter your choice: '
                    )

        if git_option == '1':upload_github()
        elif git_option == '2': git_remote_v()
        elif git_option == '3': git_remove()
        elif git_option == '4': git_clone()
        elif git_option == '5': git_push()
        elif git_option == '6': git_checkout()
        elif git_option == '7': git_merge()
        elif git_option == '8': git_branch()
        elif git_option == '9': git_pull()
        else: print('\n******************** EXIT GIT ********************\n\n')