# -*- coding:utf-8 -*-

import os
import sys

def get_home_dir(file):
    u""" アプリケーションのホームディレクトリを返します
    """
    return os.path.split(os.path.dirname(os.path.abspath(file)))[0]

def append_home_to_path(file):
    u""" アプリケーションのホームディレクトリをsys.pathに追加します
    """
    sys.path.insert(0, get_home_dir(file))
