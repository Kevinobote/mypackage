from setuptools import setup, find_packages

setup(
    name='myPackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    description='EDSA example python package',
    install_requires=['numpy'],
    author='Hineni',
    author_email='kevinobote49@gmail.com',
    url='https://github.com/Kevinobote/PythonPackage',
    license='MIT',
)