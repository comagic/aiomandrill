from setuptools import setup
import os.path

setup(
    name='aiomandrill',
    version='0.1',
    author='Anton Sychugov',
    author_email='a.sychugov@uiscom.ru',
    description='Python API library for the Mandrill email as a service '
                'platform based on original Mandrill Python API library and aiohttp',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    license='Apache-2.0',
    keywords='mandrill email api',
    url='https://github.com/comagic/aiomandrill',
    packages=['aiomandrill'],
    install_requires=['aiohttp >= 0.21.6'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Communications :: Email'
    ]
)
