from setuptools import setup, find_packages
from typing import List




Hyphen_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if Hyphen_E_DOT in requirements:
            requirements.remove(Hyphen_E_DOT)
    return requirements



setup(
    name='MLProject',
    version='0.1',
    author='Meenakshi',
    author_email='mksundar00@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    



)