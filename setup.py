import os
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

PACKAGE_NAME = 'ha-philipsjs'
HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.1.0'

PACKAGES = find_packages(exclude=['tests', 'tests.*', 'dist', 'ccu', 'build'])

REQUIRES = [
    "cryptography"
]

setup(
        name=PACKAGE_NAME,
        version=VERSION,
        license='MIT License',
        url='https://github.com/danielperna84/ha-philipsjs',
        download_url='https://github.com/danielperna84/ha-philipsjs/tarball/'+VERSION,
        author='Daniel Perna',
        author_email='danielperna84@gmail.com',
        description='jointSPACE API for Home-Assistant',
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        platforms='any',
        install_requires=REQUIRES,
        keywords=['jointSPACE'],
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.8'
        ],
        extras_require={
            'tests': [
                'pytest>3.6.4',
                'pytest-cov<2.6',
                'coveralls',
                'pytest-mock',
                'requests-mock'
            ]
        },
        python_requires='>=3.8'
)
