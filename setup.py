from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the List of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
name='machine_Learening',
version='0.0.1',
auther='anil choudhary',
auther_email='anil341518@gmail.com',
packges=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)  