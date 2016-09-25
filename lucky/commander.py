# -*- coding: utf-8 -*-

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
        self.args = args[1:]
        self.action = args[1]

    def register(self, cmd):
        """
        注册命令的装饰器
        """
        def decorator(f):
            self.commands[cmd] = f
            return f
        return decorator

    def execute(self):
        func = self.commands[self.action]
        func(*self.args)

def install_commands(cmder):
    @cmder.register('new_post')
    def new_post(*args):
        print(args)
