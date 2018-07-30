
import os
from setuptools import find_packages, setup

# Package meta-data.
NAME = 'StemRules'
DESCRIPTION = 'One-stop app for Stem info'
URL = 'https://github.com/srinidhinandakumar/codehouse'
EMAIL = 'shalini.bhaskara91@gmail.com'
AUTHOR = 'Team3-CodeHouse'
REQUIRES_PYTHON = '>=3.0.0'
VERSION = '1.0'

REQUIRED = [
    'flask'
]

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
)
