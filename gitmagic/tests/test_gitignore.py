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
        """remove created files in test dir"""
        os.removedirs('.git')
        # remove any language transferred files
        for f in os.listdir(os.getcwd()):
            if f.endswith('.gitignore'):
                os.remove(f)

    def test_add_gitignore_languages(self):
        """test core programming language gitignores are available"""
        languages = [
            'python',
            'java',
            'c++',
            'c',
            'common',
            'eclipse',
            'go',
            'haskell',
            'jboss',
            'perl',
            'r',
            'ruby',
            'scala',
            'vim',
            'windows',
        ]

        for lang in languages:
            self.GC.return_gitignore_file(language=lang)
            self.assertIn('{lang}.gitignore'.format(lang=lang), os.listdir(os.getcwd()),
                          msg="""{lang}.gitignore not properly transferred""".format(lang=lang))

    def test_get_repo_gitignore(self):
        """test .gitignore located"""
        self.GC.get_repo_gitignore()
        gitignore = self.GC.gitignore
        self.assertIn('.gitignore', gitignore,
                      msg="""unable to locoate gitignore file""")


