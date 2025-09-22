from setuptools import setup, find_packages

setup(
    name="password-generator",
    version="new",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'passgen=src.cli:main',
        ],
    },
)