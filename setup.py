from setuptools import setup

setup(
    name='gitclean',
    version='0.0.1',
    py_modules=['cli'],
    install_requires=[
        'Click'
    ],
    entry_points='''
                [console_scripts]
                mygitclean=gitmagic:cli
    '''
)