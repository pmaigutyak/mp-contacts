
from setuptools import setup, find_packages

from contacts import __version__


with open('requirements.txt') as f:
    requires = f.read().splitlines()


url = 'https://github.com/pmaigutyak/mp-contacts'


setup(
    name='django-mp-contacts',
    version=__version__,
    description='Django contacts app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='%s/archive/%s.tar.gz' % (url, __version__),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=requires
)
