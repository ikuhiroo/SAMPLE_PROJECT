from setuptools import setup
import sys
from SAMPLE_PROJECT import (
    __author__,
    __author_email__,
    __app__,
    __version__,
    __release__,
    __prog__
)

# validation
if sys.version_info < (3, 4):
    print("Building SAMPLE_PROJECT requires at least Python 3.4 to run.")
    sys.exit(1)

setup(name=__app__,
      version= "{}.{}".format(__version__, __release__),
      description='hogehoge tool',
      long_description="""this supports to hogehoge.""",
      author=__author__
      author_email=__author_email__
      url='https://github.com/masudak/hogehoge',
      packages=[
          'SAMPLE_PROJECT' # __init__.pyを置いてあるので、これでモジュール化できる
          ],
      py_modules=[
          # 上記のpackagesで収まるので、特に使わない
          ],
      zip_safe = (sys.version>="2.5"), #2.5の頃はディレクトリとしてegg作らないとまずかった？
      scripts=[
          'bin/command1',
          'bin/command2'
          ],
      license='GNU Lesser General Public License v3 or later (LGPLv3+)',
      keywords='',
      platforms='Linux',
      classifiers=['Intended Audience :: System Administrators',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
                   'Natural Language :: Japanese',
                   'Programming Language :: Python :: 3.4',
                   ],
      )
