# -*- coding: utf-8 -*-

import os
import sys
import json

from collections import UserDict

# 用户当前工作目录
CURT_PATH = os.path.realpath(os.curdir)
POST_PATH = os.path.join(CURT_PATH, '_posts')

# 源码根目录
ROOT_PATH = os.path.realpath(os.path.join(__file__, '../../'))

class Config(UserDict):
    def __init__(self):
        """
        用于加载config.json配置文件
        """
        pathname = os.path.join(CURT_PATH, 'config.json')

        with open(pathname) as f:
            __dict__ = json.load(f)
            super(Config, self).__init__(__dict__)

_config = Config()
