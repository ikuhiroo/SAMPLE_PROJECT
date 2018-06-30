# -*- coding:utf-8 -*-

# パスを通す
import sys
sys.path.append('/Users/ikuhiro/Desktop/SAMPLE_PROJECT')

from SAMPLE_PROJECT import log
from SAMPLE_PROJECT.constants import CONSTANTS
# from SAMPLE_PROJECT.lock import create_lock_file
# from SAMPLE_PROJECT.lock import delete_lock_file
from SAMPLE_PROJECT.util import check_python_version
from SAMPLE_PROJECT.util import retrieve_env
# from SAMPLE_PROJECT.util import check_exec_user
import argparse

def argument_parse():
    __description='This script is...'
    parser = argparse.ArgumentParser(description=__description)
    parser.add_argument('-f',
        dest='config_file',
        default=None,
        help='設定ファイルを指定してください。',
        required=True
    )
    __args = parser.parse_args()
    return __args


# メイン処理開始
if __name__ == '__main__':

    # __args = argument_parse()

    # Lock作成
    # create_lock_file()

    # ここに実処理書く
    __env = retrieve_env()
    print(CONSTANTS[__env]['apps']['EXEC_USER'])

    print(check_python_version())

    # Lock解除
    # delete_lock_file()
