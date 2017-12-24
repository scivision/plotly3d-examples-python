#!/usr/bin/env python
install_requires = ['numpy', 'plotly']
tests_require = ['nose','coveralls']
# %%
from setuptools import setup, find_packages

setup(name='plotly3d-examples-python',
      packages = find_packages(),
      version = '0.1.0',
      description='Simple 3D plots with Plotly offline/free.',
      long_description=open('README.rst').read(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/plotly3d-examples-python',
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests':tests_require},
      python_requires='>=2.7')
