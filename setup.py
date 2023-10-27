from setuptools import setup, find_packages

setup(
    name='simplehand',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    description='A simple 3D hand visualizer',
    author='Joey Costello',
    author_email='your_email@example.com',
    url='https://github.com/jtcostello/simple-mpl-hand',
)
