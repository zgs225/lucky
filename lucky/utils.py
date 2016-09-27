# -*- coding: utf-8 -*-

import re
import os
import sys
import datetime
import tempfile

from . import pinyin
from .config import POST_PATH

def uri_case(title):
    """
    将字符串转换成网页链接形式
    """
    title = pinyin.get(title)
    title = title.lower().rstrip()
    title = re.sub(r'\s+', '-', title)
    return title

def create_new_post(post_name):
    today = datetime.date.today()
    fullname = '%s-%s.markdown' % (
        today.strftime('%Y-%m-%d'), uri_case(post_name))
    pathname = os.path.join(POST_PATH, fullname)

    if os.path.exists(pathname):
        answer = input('文件已经存在，要覆盖吗？(Y/n)')

        if answer is not 'Y':
            print('中断')
            sys.exit(1)

    with tempfile.NamedTemporaryFile(delete=False) as fp:
        fp.write(bytearray('你好', 'utf-8'))
        os.rename(fp.name, pathname)

        print('创建： %s' % pathname)
