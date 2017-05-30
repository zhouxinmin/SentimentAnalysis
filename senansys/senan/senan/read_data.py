# ! /usr/bin/env python
# -*- coding: utf-8 --
# ---------------------------
# @Time    : 2017/5/29 11:44
# @Site    : 
# @File    : read_data.py
# @Author  : zhouxinmin
# @Email   : 1141210649@qq.com
# @Software: PyCharm

import os
import sys
import xmlParser
import copy
# from Timer import Timer
from Translator import Translator

ROOT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
DATA_DIR = os.path.join(ROOT_DIR, "data")
TRAIN_DATA_DIR = "Train_EN"
UNLABEL_DATA_DIR = "Unlabel_CN"
VALIDATION_DATA_DIR = "Train_CN"

TRAIN_DATA_BOOK = os.path.join(DATA_DIR, TRAIN_DATA_DIR, "book", "train.data")
TRAIN_DATA_DVD = os.path.join(DATA_DIR, TRAIN_DATA_DIR, "dvd", "train.data")
TRAIN_DATA_MUSIC = os.path.join(DATA_DIR, TRAIN_DATA_DIR, "music", "train.data")

UNLABEL_DATA_BOOK = os.path.join(DATA_DIR, UNLABEL_DATA_DIR, "book", "unlabel.data")
UNLABEL_DATA_DVD = os.path.join(DATA_DIR, UNLABEL_DATA_DIR, "dvd", "unlabel.data")
UNLABEL_DATA_MUSIC = os.path.join(DATA_DIR, UNLABEL_DATA_DIR, "music", "unlabel.data")

VALIDATION_DATA_BOOK = os.path.join(DATA_DIR, VALIDATION_DATA_DIR, "book", "sample.data")
VALIDATION_DATA_DVD = os.path.join(DATA_DIR, VALIDATION_DATA_DIR, "dvd", "sample.data")
VALIDATION_DATA_MUSIC = os.path.join(DATA_DIR, VALIDATION_DATA_DIR, "music", "sample.data")

train_file_en = [TRAIN_DATA_BOOK, TRAIN_DATA_DVD, TRAIN_DATA_MUSIC]
unlabel_file_cn = [UNLABEL_DATA_BOOK, UNLABEL_DATA_DVD, UNLABEL_DATA_MUSIC]
validation_file_cn = [VALIDATION_DATA_BOOK, VALIDATION_DATA_DVD, VALIDATION_DATA_MUSIC]


def import_data():
    train_data_en, unlabel_data_cn, validation_data_cn = [], [], []
    parser = xmlParser.XMLParser()

    for filename in train_file_en:
        train_data_en += parser.parse(filename)
    for filename in unlabel_file_cn:
        unlabel_data_cn += parser.parse(filename)
    for filename in validation_file_cn:
        validation_data_cn += parser.parse(filename)
    return train_data_en, unlabel_data_cn, validation_data_cn


def __translate_dataset(translate_method, src_dataset):
    # Use translate_method to translate src_dataset into dst_dataset
    dst_dataset = []
    for item in src_dataset:
        dst_item = {}
        for attr in item:
            if attr in ['summary', 'text']:
                dst_item[attr] = translate_method(item[attr])
            else:
                dst_item[attr] = item[attr]
        dst_dataset.append(copy.deepcopy(dst_item))
    return dst_dataset


def translate():
    # Translate all datasets
    train_data_en, unlabel_data_cn, validation_data_cn = import_data()
    translator = Translator()

    train_data_cn = __translate_dataset(translator.en_to_cn, train_data_en)
    unlabel_data_en = __translate_dataset(translator.cn_to_en, unlabel_data_cn)
    validation_data_en = __translate_dataset(translator.cn_to_en, validation_data_cn)

    print "train_data_cn", train_data_cn
    print "unlabel_data_en", unlabel_data_en
    print " validation_data_en",  validation_data_en
    return train_data_cn, unlabel_data_en, validation_data_en

