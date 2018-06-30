# -*- coding:utf-8 -*-

# パスを通す
import sys
sys.path.append('/Users/ikuhiro/Desktop/SAMPLE_PROJECT')

import os
import constants

def check_python_version() -> None:
    u""" 実行されているPythonのバージョンが許可したバージョンかの確認を行います。
    """
    python_version = __get_python_version()
    expected_python_version = Constants.get_python_version()
    from hogehoge import log
    log.output(u"REAL PYTHON VERSION: %s, EXPECTED PYTHON VERSION: %s"
            % (python_version, expected_python_version)
    )
    if python_version != expected_python_version:
        raise Exception('このPythonバージョンでの実行は許可されていません')


def __get_python_version():
    u""" 実行されているPythonのバージョンを取得します。
    sys.version_info(major=3, minor=6, micro=3, releaselevel='final', serial=0)
    sys.version_info[0] = 3
    sys.version_info[0] = 6
    sys.version_info[0] = 3
    """
    __python_version = '%i.%i.%i' % (
        sys.version_info[0],
        sys.version_info[1],
        sys.version_info[2])
    return __python_version

def get_home_dir(file):
    u""" アプリケーションのホームディレクトリを返します。
    """
    return os.path.split(os.path.dirname(os.path.abspath(file)))[0]

def retrieve_env():
    u""" 環境変数を参照し、スクリプト実行環境を判別します。

         実行時デフォルトはdefaultを返すようになっています
         「SCRIPT_ENV=production hogehoge.py」のように実行することで、
         環境に応じたコンフィグを得ることができます。
    """
    __env = 'DEFAULT'
    if 'SCRIPT_ENV' in os.environ:
        __env = os.environ['SCRIPT_ENV']
    return __env
