# -*- coding: utf-8 -*-

import re
import csv
import os.path

from .config import ROOT_PATH

"""
将汉字转换成拼音
"""

pinyin_dict = {}

datapath = os.path.join(ROOT_PATH, 'lucky/Mandarin.dat')

with open(datapath) as tsv:
    for line in csv.reader(tsv, delimiter='\t'):
        pinyin_dict[line[0]] = line[1]

def _char_to_pinyin(c):
    k = '%X' % ord(c)
    v = pinyin_dict[k]

    return v

def _single_pinyin(pinyin):
    return not ' ' in pinyin

def _char_tone(pinyin):
    if _single_pinyin(pinyin):
        return pinyin[:-1], int(pinyin[-1:])
    else:
        return _char_tone(pinyin.split(' ')[0])

def _get(s, delimiter = '-'):
    s = s.strip()
    result = []
    flag = True

    for c in s:
        try:
            pinyin = _char_to_pinyin(c)
            pinyin, tone = _char_tone(pinyin)
            result.append(pinyin)
            flag = True
        except KeyError:
            if flag:
                result.append(c)
            else:
                result[-1] += c
            flag = False

    return delimiter.join(result)

def get(s, delimiter = '-'):
    """
    将汉字转换成拼音，获得全拼；如果是其他字符，则返回

    :param s: unicode字符
    """
    return delimiter.join(map(_get, re.split('\s+', s)))
