from setuptools import setup,find_packages

## Setup function
setup(
    name = "ML project - 1",
    version = '0.0.1',
    author = "Shashank",
    author_email = 'shashankashashi2001@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas','flask'],

)