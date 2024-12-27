
from setuptools import setup, find_packages

setup(
    name='chatassist',
    version='0.1.0',
    description='A Python library for handling ChatGPT interactions.',
    author='Daryoush Alipour',
    author_email='ai.tirotir@gmail.com',
    packages=find_packages(include=['chatassist', 'chatassist.*']),
    install_requires=[
        'requests',
        'argparse',
        'tk'
    ],
    entry_points={
        'console_scripts': [
            'chatassist-cli=chatassist.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
