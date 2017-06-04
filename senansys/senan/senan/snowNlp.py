# ! /usr/bin/env python
# -*- coding: utf-8 --
# ---------------------------
# @Time    : 2017/5/30 16:38
# @Site    : 
# @File    : snowNlp.py
# @Author  : zhouxinmin
# @Email   : 1141210649@qq.com
# @Software: PyCharm

from snownlp import SnowNLP


def cal_hold_press(value):
    value *= 100
    if 0 <= value <= 60:
        return "progress-bar-danger"
    elif 60 < value <= 70:
        return "progress-bar-warning"
    elif 70 < value <= 80:
        return "progress-bar-secondary"
    elif 80 < value <= 90:
        return "progress-bar-success"
    elif 100 < value:
        return "progress-bar-danger"
    else:
        return "progress-bar-warning"


def get_mood(sentence):
    text = unicode(sentence)
    print text
    s = SnowNLP(text)
    pro = s.sentiments
    temp_hold1 = '%.2f%%' % (pro * 100)
    score = '%.2f' % (pro * 100)
    return {'predict': [cal_hold_press(pro), temp_hold1, score]}
