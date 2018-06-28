import os

def is_over_hundred(file):
    """
    check if file size is greater than 100mb

    :param file:
    :return: boolean
    """
    fsize = os.path.getsize(file) >> 20
    if fsize > 100:
        return True


def is_gitignore(repo_root):
    """
    check if .gitignore is present in root of repo

    :param repo_root: root repo directory
    :return: boolean
    """
    return any([file.lower().endswith('.gitignore') for file in os.listdir(repo_root)])