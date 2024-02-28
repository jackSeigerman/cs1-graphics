from setuptools import setup, find_packages

setup(
    name='cs1-graphics',
    version='1.2',
    packages=find_packages(),
    install_requires=['turtle'],
    author='Jack Seigerman',
    author_email='jacks3ds@gmail.com',
    description='python 3 drawing library that takes calls similar to the cs1-graphics library and outputs with the '
                'turtle library',
    long_description_content_type='text/markdown',
    long_description='Please keep in mind that this is still a work in progress. This project was made because the '
                     'pre existing cs1 graphics library does not work with python3. This library takes calls that '
                     'would work with cs1.graphics and renders the image in turtle instead.',
    url='https://github.com/jackSeigerman/cs1-graphics',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
