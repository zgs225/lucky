# -*- coding: utf-8 -*-

import os
import sys
import json

from collections import UserDict

ROOT_PATH = os.path.realpath(os.path.join(__file__, '../../'))

def root_path():
    """
    获取项目的真是根目录地址
    """
    return ROOT_PATH

class Config(UserDict):
    def __init__(self):
        """
        用于加载config.json配置文件
        """
        pathname = os.path.join(ROOT_PATH, 'config.json')

        with open(pathname) as f:
            __dict__ = json.load(f)
            super(Config, self).__init__(__dict__)

_config = Config()
