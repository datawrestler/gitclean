import unittest
import os

from gitmagic.git_clean import GitClean


class BaseTest(unittest.TestCase):
    """base test with standard setup and teardown methods"""

    def setUp(self):
        # create .git directory
        if not os.path.exists('.git'):
            os.makedirs('.git')
        # create .gitignore
        with open('.gitignore', 'w') as outfile:
            outfile.write('gitignore file')
            outfile.close()

        self.GC = GitClean(os.getcwd())
        self.GC.find_repo_root(os.getcwd())

    def tearDown(self):
        """remove created files in test dir"""
        os.removedirs('.git')
        if os.path.exists('large_file.txt'):
            os.remove('large_file.txt')
        # remove any language transferred files
        for f in os.listdir(os.getcwd()):
            if f.endswith('.gitignore'):
                os.remove(f)


class TestGitIgnoreMixin(BaseTest):

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


class TestLargeFileMixin(BaseTest):

    def setUp(self):
        # create .git directory
        if not os.path.exists('.git'):
            os.makedirs('.git')

        # create large file
        gig = int((1024*1024*1024)/95)
        with open('large_file.txt', 'wb') as outfile:
            outfile.write(os.urandom(gig))

        self.GC = GitClean(os.getcwd())
        self.GC.find_repo_root(os.getcwd())
        self.GC.return_gitignore_file()
        self.GC.get_repo_gitignore()

    def test_traverse_large_file(self):
        """test large files located and written in gitignore"""
        self.GC.traverse_large_files(max_file_size=10)
        with open(self.GC.gitignore, 'r') as infile:
            lines = infile.readlines()
            infile.close()

        self.assertIn('large_file.txt', lines[-1],
                      msg="""large_file not written to gitignore""")

    def test_write_large_file(self):
        """test large file written to gitignore"""
        self.GC.write_large_file('test_large_file.txt')
        with open(self.GC.gitignore, 'r') as infile:
            lines = infile.readlines()

        self.assertEqual(lines[-1], 'test_large_file.txt',
                         msg="""test_large_file.txt not written to gitignore""")

class TestGitClean(BaseTest):

    def test_find_repo_root(self):
        """Test identification of repo root"""
        self.GC.find_repo_root(os.getcwd())
        self.assertEqual(self.GC.repo_root, os.getcwd(),
                        msg="""repo root different than called dir""")





