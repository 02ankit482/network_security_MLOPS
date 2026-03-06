'''
this is the setup file for the package. It is used to install the package and its dependencies.
'''

from setuptools import setup, find_packages, setup 
from typing import List

def get_requirements()->List[str]:
    '''
    this function is used to get the requirements from the requirements.txt file.
    '''
    requirement_lst:List[str]=[]
    try:
       with open('requirements.txt','r') as file:
           #read each line
           lines=file.readlines()
           #process_eaach_line
           for line in lines:
               requirement=line.strip()
               ##ignpre any empty lines
               if requirement and requirement!='-e .':
                   requirement_lst.append(requirement)
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
    return requirement_lst
print(get_requirements())

setup(
    name='network_security_MLOPS',
    version='0.0.1',
    author='Ankit Yadav',
    packages=find_packages(),
    install_requires=get_requirements()
)