from setuptools import setup

setup(
    name='gitmagic',
    description='Easy, one line, git commands to control large files',
    keywords='git github gitlab lfts',
    version='0.0.1',
    py_modules=['cli'],
    install_requires=[
        'Click'
    ],
    entry_points='''
                [console_scripts]
                mygitclean=gitmagic.gitmagic:cli
    ''',
    package_data={'gitmagic.gitignore_examples': ['*']},
    include_package_data=True,
    author='Jason Lewris',

)