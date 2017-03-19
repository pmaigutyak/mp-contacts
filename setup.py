
from setuptools import setup, find_packages

from contacts import __version__


setup(
    name='django-mp-contacts',
    version=__version__,
    description='Django contacts app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-contacts',
    download_url='https://github.com/pmaigutyak/mp-contacts/archive/%s.tar.gz' % __version__,
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'django-widget-tweaks==1.4.1',
        'django-recaptcha==1.2.1'
    ]
)
