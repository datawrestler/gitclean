import unittest
import os

from gitmagic.git_clean import GitClean


class TestGitIgnoreMixin(unittest.TestCase):

    def setUp(self):
        # create .git directory
        if not os.path.exists('.git'):
            os.makedirs('.git')
        # create .gitignore
        with open('.gitignore', 'w') as outfile:
            outfile.write('gitignore file')
            outfile.close()

        self.GC = GitClean(os.getcwd())
        self.GC.get_repo_root(os.getcwd())

    def tearDown(self):
        os.removedirs('.git')
        os.remove('.gitignore')

    def test_get_repo_gitignore(self):
        """test .gitignore located"""
        self.GC.get_repo_gitignore()
        gitignore = self.GC.gitignore
        self.assertIn('.gitignore', gitignore,
                      msg="""unable to locoate gitignore file""")


