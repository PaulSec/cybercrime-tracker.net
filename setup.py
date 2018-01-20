from setuptools import setup

setup(
    name='cybercrimetracker',
    author='PaulSec',
    author_email='paulwebsec@gmail.com',
    version='0.0.2',
    packages=['cybercrimetracker'],
    description='(Unofficial) Python API for cybercrime-tracker',
    install_requires=["bs4", "requests"],
    url = 'https://github.com/PaulSec/cybercrime-tracker',
    download_url = 'https://github.com/PaulSec/cybercrime-tracker/archive/0.0.2.tar.gz',
    keywords = ['cybercrime-tracker', 'c2c', 'malwares', 'osint'],
)