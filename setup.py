from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'ratio_merge',
  packages = ['ratio_merge'],
  version = '0.3',
  description = 'A small utility function for merging two lists by some ratio',
  long_description=long_description,
  author = 'Adam Lev-Libfeld',
  author_email = 'adam@tamarlabs.com',
  license='Apache 2.0',
  url = 'https://github.com/daTokenizer/ratio-merge-python',
  download_url = 'https://github.com/daTokenizer/ratio-merge-python/archive/0.2.tar.gz',
  keywords = ['merge', 'ratio', 'lists'], # arbitrary keywords
  classifiers = [],
)
