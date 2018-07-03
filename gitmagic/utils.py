import os


def is_large(file, max_file_size=100):
    """
    check if file size is greater than max_file_size mb's

    :param file: str - file path to test size of
    :return: boolean
        True - file larger than max_file_size
        False - file smaller than max_file_size
    """
    fsize = os.path.getsize(file) >> 20
    if fsize >= float(max_file_size):
        return True
    else:
        return False


def is_gitignore(repo_root):
    """
    check if .gitignore is present in root of repo

    :param repo_root: root repo directory
    :return: boolean
    """
    return any([file.lower().endswith('.gitignore') for file in os.listdir(repo_root)])


