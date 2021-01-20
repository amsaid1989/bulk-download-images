# Copyright 2021 Abdelrahman Said
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from setuptools import setup, find_packages
import pathlib
from src.dwimgs.utils import package_info

# Get the source directory of the setup.py file
source_dir = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README.md file
l_description = pathlib.Path(source_dir / 'README.md'). \
    read_text(encoding='utf-8')

setup(name=package_info.name,
      version=package_info.version,
      description='Command line utility to bulk download images from ' \
                  'a text file',
      long_description=l_description,
      long_description_content_type='text/markdown',
      author=package_info.author,
      author_email='said.abdelrahman89@gmail.com',
      url='https://github.com/amsaid1989/bulk-download-images',
      package_dir={'': 'src/dwimgs'},
      packages=find_packages(where='src/dwimgs'),
      py_modules=['run'],
      license='MIT',
      platforms=['OS Independent'],
      install_requires=['requests'],
      entry_points={
          'console_scripts': ['dwimgs=run:main']
      },
      )
