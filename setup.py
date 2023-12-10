from setuptools import setup, find_packages

setup(
    name='simplehand',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    description='A simple 3D hand visualizer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joey Costello',
    author_email='your_email@example.com',
    url='https://github.com/jtcostello/simplehand',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
