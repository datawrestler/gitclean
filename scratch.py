import os
import sys
import warnings
from shutil import copy2

from utils import is_gitignore, is_over_hundred

called_dir = '/Users/jasonlewris/Desktop/GitProjects/gitclean'

language = 'python'


class GitIgnoreMixin(object):
    """Mixin class for all gitignore operations"""

    def return_gitignore_file(self,
                              language='python'):
        """
        return a sample gitignore based on the programming language

        :param language: programming language
        :return: gitignore fpath
        """

        if not hasattr(self, 'repo_root'):
            raise RuntimeError("""repo_root needs to be identified prior to calling 
            return_gitignore_file""")

        # TODO anchor gitignore dir down so its found in the sample place everywhere
        all_ignores = os.listdir('gitignore')

        gitignore = list(filter(lambda x: x.split('.')[0].lower() == language, all_ignores))

        if len(gitignore) == 1:
            copy2(os.path.join('gitignore', gitignore[0]), self.repo_root)
        else:
            warnings.warn("""Unable to locate relevant gitignore config""")

    def get_repo_gitignore(self):
        """
        assign root gitignore file to instance

        :return: N/A
        """
        gitignore = list(filter(lambda x: x.lower().endswith('.gitignore'), os.listdir(self.repo_root)))
        self.gitignore = os.path.join(self.repo_root, gitignore)

class LargeFileMixin(object):
    """Mixin for large file operations"""

    def write_large_file(self, lg_file_path):
        """
        Write new line in gitignore for large files
        :param lg_file_path: full path to large file
        :return: N/A
        """

        with open(self.gitignore, 'a') as outfile:
            outfile.write(lg_file_path)
            outfile.close()

class GitClean(GitIgnoreMixin):

    def __init__(self, called_dir):
        self.called_dir = called_dir

    def get_repo_root(self, called_dir, recursion_level=0):
        """
        get the root directory of current repo
        :param called_dir:
        :return:
        """

        # if the function has traveresed too long, give up and raise error
        if recursion_level > 20:
            raise RuntimeError("""Unable to locate repo root directory. Ensure repo 
            is initialized with .git""")

        for root, dirs, files in os.walk(called_dir, topdown=True):
            if '.git' in dirs:
                self.repo_root = os.path.join(root)
                return self

        # otherwise step back a directory and try again
        parent, dir = os.path.split(called_dir)
        self.get_repo_root(parent, recursion_level + 1)





with open('Python.gitignore', 'a') as outfile:
    outfile.write('largefile.csv')

GC = GitClean(called_dir)

GC.get_repo_root(called_dir)
GC.repo_root
def return_gitignore_file(repo_root,
                          language='python'):
    """
    return a sample gitignore based on the programming language

    :param language: programming language
    :return: gitignore fpath
    """
    # TODO anchor gitignore dir down so its found in the sample place everywhere
    all_ignores = os.listdir('gitignore')

    gitignore = list(filter(lambda x: x.split('.')[0].lower() == language, all_ignores))

    if len(gitignore) == 1:
        copy2(os.path.join('gitignore', gitignore[0]), repo_root)
    else:
        warnings.warn("""Unable to locate relevant gitignore config""")






os.path.getsize('scratch.py') >> 20

if __name__ == '__main__':
    print(os.getcwd())