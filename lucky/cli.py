#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
命令集中区
"""

# 将项目路径加入到sys.path中

import os
import sys

from .config import ROOT_PATH
from .commander import Commander, install_commands

def main():
    cmder = Commander(*sys.argv)
    install_commands(cmder)
    cmder.execute()

if __name__ == '__main__':
    main()
