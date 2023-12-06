from setuptools import setup,find_packages
from typing import List

def get_requirements(path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [each_item.strip() for each_item in requirements 
        if "# " not in each_item and 
        each_item!="\n" and each_item!="-e ."]
    return requirements


## Setup function
setup(
    name = "ML project - 1",
    version = '0.0.1',
    author = "Shashank",
    author_email = 'shashankashashi2001@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)