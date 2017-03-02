# coding:utf-8

import jieba
import copy
# from nltk.book import *
# from nltk.corpus import names
# import random

seg_list = jieba.cut("项目针对现实生活中的不确定性，系统研究不确定性理论，具有重要的理论意义和研究价值。项目组具有"
                     "深厚的研究基础，发表了大量学术论文，从事了很多有价值的研究课题，研究水平很高。从申请项目的研"
                     "究内容描述中，研究内容“完善不确定性信息的概念及信息的描述方法，完善不确定性信息理论体系”，"
                     "“完善不确定性系统理论基础”，“完善不确定性数学理论基础”，申请人要完善的具体内容是什么，"
                     "完善的内容涉及哪些方面？申请人并没有过多描述。“建立多维动态分析模型”，与“不确定性系统理"
                     "论基础”的联系何在。项目提出“工业过程控制中”的应用，但是并没有描述工业过程控制中的应用"
                     "对象的特点。此外，从研究现状的描述来看，申请者提出本申请项目是已有国家自然科学基金的延续，"
                     "但是，申请人并没有阐述现有研究的“不完善”之处。由此，项目提出了完善现有研究，内容显得笼统，"
                     "研究预期成果并不明确。建议申请人在下一阶段的研究过程中进一步明确现有研究的"
                     "不完善之处和需要研究的内容。", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))  # 精确模式


seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
print list(seg_list)

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print list(seg_list)
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))


