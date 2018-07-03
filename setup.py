from setuptools import setup

setup(
author='Jason Lewris',
    author_email='datawrestler@gmail.com',
    name='gitmagic',
    version='0.0.2',
    description='Easy, one line, git commands to control large files',
    keywords='git github gitlab lfts',
    py_modules=['cli'],
    install_requires=[
        'Click'
    ],
    entry_points='''
                [console_scripts]
                gitmagic=gitmagic.gitmagic:cli
    ''',
    package_data={'gitmagic.gitignore_examples': ['*']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools'
    ]


)