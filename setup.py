from setuptools import setup

setup(
    name="ah-cli",
    version="1.0.0",
    py_module=['ahcli'],
    install_requires=[
        'Click',
        'pytest'
    ],
    entry_points='''
    [console_scripts]
    ahcli=ahcli:cli
    ''',
)