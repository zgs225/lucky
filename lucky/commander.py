# -*- coding: utf-8 -*-

import os.path
import argparse

from .utils import create_new_post

class Commander(object):
    """
    用于保存命令的字典，对应：
    command: function
    """
    commands = {}

    def __init__(self, *args):
        """
        Keyword Arguments:
        *args -- array of arguments like sys.argv
        """
        parser = argparse.ArgumentParser(description='Lucky static site generator')
        parser.add_argument('action', default='new_post')
        namespace, remains = parser.parse_known_args(args[1:])

        self.parser = parser
        self.action = namespace.action
        self.args   = remains

    def register(self, cmd):
        """
        注册命令的装饰器
        """
        def decorator(f):
            self.commands[cmd] = f
            return f
        return decorator

    def execute(self):
        try:
            func = self.commands[self.action]
        except KeyError:
            print(self.parser.format_help())
        else:
            func(*self.args)

def install_commands(cmder):
    @cmder.register('new_post')
    def new_post(*args):
        create_new_post(args[0])
