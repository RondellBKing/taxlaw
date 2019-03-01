from setuptools import setup


setup(
   name='taxlaw',
   version='1.0.0', #sementic versioning https://semver.org/
   description='Code to mine public records and find people in tax distress.',
   license='',
   author='Mitchell Hall',
   author_email='mitchellanthonyhall@gmail.com',
   url='https://github.com/RondellBKing/taxlaw',
   packages=find_packages(),
   install_requires=['', ''], #external packages as dependencies
   python_requires='>=3.6.6'
)
