#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/AD1D1/DSSS-HW5-Aditya-1.git',
    author='Aditya Dixit',
    author_email='adityajdixit2@@gmail.com',

    py_modules=['my_pip_package'],
)

