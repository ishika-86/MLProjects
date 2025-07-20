from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns list of requirements from a requirements.txt file
    '''
    requirements =[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements ]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Ishika Bansal',
    author_email='ishikabansal523@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
