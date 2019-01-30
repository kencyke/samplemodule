import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'sample', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

with open('HISTORY.md', 'r') as f:
    history = f.read()

with open('LICENSE', 'r') as f:
    license_ = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    url='https://github.com/kencyke/samplepmodule',
    license=license_,
    author='kencyke',
    packages=find_packages(exclude=['tests', 'dist']),
    python_requires=">=3.6"
)
