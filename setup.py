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
   install_requires=[
   'beautifulsoup4 == 4.7.1',
   'flask == 1.0.2',
   'lxml == 4.3.1',
   'pygsheets == 2.0.0'
   ],
   python_requires='>=3.6.6'
)
