import os, sys, re, codecs
from setuptools import setup, find_packages

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

long_description = read('README.rst')

setup(name="tailpy",
      version="0.1",
      description="Efficient python log tailer using libuv.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
#          'Programming Language :: Python :: 3',
#          'Programming Language :: Python :: 3.1',
#          'Programming Language :: Python :: 3.2',
#          'Programming Language :: Python :: 3.3',
      ],
      keywords='logs tail libuv epoll kqueue iocp tailf',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["contrib", "docs", "tests*"]),
      package_data={},
      install_requires=['pyuv',],
      entry_points=dict(console_scripts=['tail=tailpy:tail',]),
      zip_safe=False,
)
