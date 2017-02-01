
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='mp-contacts',
    version='1.0.0',
    description='Django contacts app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-contacts',
    packages=['contacts'],
    license='MIT',
    install_requires=[
        'django-widget-tweaks==1.4.1',
        'django-recaptcha==1.2.1'
    ]
)
