# coding:utf-8
import jieba
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def load_key_words(file_path):
    fp = open(file_path)
    lines = fp.readlines()
    lines = [line.replace("\n", "") for line in lines]
    return lines


def build_key_word(path):
    """
    通过词频产生key word
    :param path:
    :return:
    """
    d = {}
    # with open(path, encoding="utf-8") as fp:
    fp = open(path)
    for line in fp:
        for word in jieba.cut(line.strip()):
            if len(word) > 1:  # 避免大量无意义的词语进入统计范围
                d[word] = d.get(word, 0) + 1
    kw_list = sorted(d, key=lambda x: d[x], reverse=True)
    # 取前0.5名
    size = int(len(kw_list) * 0.2)
    return kw_list[:size]


def _get_feature(sentence, key_word):
    size = len(key_word)
    feature = [0 for _ in range(size)]
    for index in range(size):
        word = key_word[index]
        value = sentence.find(word)  # 单词最初出现的位置
        if value != -1:
            feature[index] = 1
    return np.array(feature)


def get_feature(path, kw_list):
    features = []
    # lines = []
    label = []
    fp = open(path)
    for line in fp:
        temp = line.strip()
        try:
            s = temp.split("---")
            sentence = s[0]
            label.append(int(s[1]))
            features.append(_get_feature(sentence, kw_list))
        except Exception:
            print(temp + " error")
            continue
    return features, label


def script_run(sentence):
    # 产生keyword
    kw_list = build_key_word("C:/Users/zhouxinmin/PycharmProjects/Sentiment analysis/senansys/senan/file/train.txt")
    # 保存数据
    fp = open("C:/Users/zhouxinmin/PycharmProjects/Sentiment analysis/senansys/senan/file/new_word.txt",
              mode="w")
    for word in kw_list:
        fp.write(word + "\n")
    fp.close()
    feature, label = get_feature("C:/Users/zhouxinmin/PycharmProjects/Sentiment analysis/senansys/senan/file/"
                                      "train.txt",
                                 kw_list)
    gnb = GaussianNB()
    # print "feature", feature
    # print "label", label
    gnb2 = gnb.fit(feature, label)
    Key_word = load_key_words("C:/Users/zhouxinmin/PycharmProjects/Sentiment analysis/senansys/senan/file/"
                                   "new_word.txt")
    feature = _get_feature(sentence, Key_word)
    pre_y = gnb2.predict([feature])
    return {'predict': pre_y[0]}
    # print(feature,label)


def get_mood(sentence, key_word, model_name):
    feature = _get_feature(sentence, key_word)
    gnb = joblib.load(model_name)
    pre_y = gnb.predict([feature])
    return pre_y
