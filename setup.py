import os

from setuptools import find_packages, setup


def read(*parts):
    with open(os.path.join(*parts), 'r') as f:
        return f.read()


def find_version(*file_paths):
    _locals = locals()
    exec(read(*file_paths), globals(), _locals)
    if '__version__' not in _locals:
        raise RuntimeError('Unable to find version string.')
    return _locals['__version__']


def install_requires():
    return read('requirements.txt')


def tests_require():
    return read('dev-requirements.txt')


setup(
    name='paylands',
    version=find_version('paylands', 'version.py'),
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires(),
    tests_require=tests_require(),
    description='Granada Dynamics Core Framework',
    url='https://www.granadadynamics.com',
    author='Granada Dynamics, SL',
    author_email='apps@granadadynamics.com',
    license='MIT License',
    zip_safe=True,
)