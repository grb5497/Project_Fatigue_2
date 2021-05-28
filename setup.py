from setuptools import find_packages, setup

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='project_fatigue_2',
    version='0.1.0',
    description='Tools for fatigue data analysis',
    author='Gisela Rosado Bailón',
    license='',
    packages=find_packages(include=['project_fatigue_2']),
    install_requires=REQUIREMENTS,
    extras_require={
        'interactive': ['jupyter', 'matplotlib']
        },
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest']
)