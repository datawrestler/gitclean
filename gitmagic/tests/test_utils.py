import unittest
import os

from gitmagic.utils import is_gitignore, is_large


class TestUtils(unittest.TestCase):

    def test_is_large_fsize(self):
        """
        assert is_large returns boolean value when fsize larger
        than max_file_size
        """

        bool_result = is_large('test_utils.py', max_file_size=0)
        self.assertEqual(bool_result, True, msg="""is_large not returning True when fsize 
                                                    greater than or equal to max_file_size""")

    def test_is_large_rtype(self):
        """test is_large returns boolean value"""

        result = is_large('test_utils.py')
        self.assertIsInstance(result, bool,
                              msg="""bool not returned by is_large""")

    def test_is_gitignore_rtype(self):
        """test bool returned from is_gitignore"""

        result = is_gitignore(os.getcwd())
        self.assertIsInstance(result, bool,
                              msg="""bool not return by is_gitignore""")

    def test_is_gitignore_find_gitignore(self):
        """assert is_gitignore can located gitignore file"""
        from pathlib import Path

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        p = Path(ROOT_DIR).parents[1]
        result = is_gitignore(p)
        self.assertEqual(result, True,
                         msg="""is_gitignore unable to locate gitignore from root directory""")
