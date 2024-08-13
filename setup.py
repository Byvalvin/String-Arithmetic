from setuptools import setup, find_packages

setup(
    name='string_arith_lib',
    version='0.1.0',
    author='Daniel Asimiakwini',
    author_email='kwini@gmail.com',
    description='interesting string logic',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Byvalvin/String-Arithmetic',
    packages=find_packages(include=['string_arith_lib', 'string_arith_lib.*']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
