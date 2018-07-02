===========================
**gitmagic** README file
===========================


Gitmagic is a simple, command line python package to make dealing with large files and git painless. It was originally created due to many painful
git commits when a data file contained in the repo was over 100mb. This would then require going back, adding the file to the gitignore or removing the tracking
history from the git log. Now with gitmagic, you can simply run the utility function before performing your commits and all files over 100mb (or user defined max_file_size)
will be automatically added to the .gitignore file.

Additionally, the best .gitignore examples from [dozens of programming languages](https://github.com/github/gitignore) can be automatically added to your repo based on your programming language.


Installation
----------------

To install gitmagic, simply use pip:

.. code-block:: python
    pip install gitmagic

Usage
------------------

Using gitmagic is easy. Simply before making your commits on your repo, run the following from the command line:

.. code-block:: console
    mygitclean --verbose --add_gitignore --language python --max_file_size 100

Parameters
-------------------

Gitmagic has a couple important parameters:

1. add_gitignore: Boolean flag - add gitignore file
2. language: str - add gitignore for programming language specified
3. max_file_size: int - add files over max_file_size to .gitignore


