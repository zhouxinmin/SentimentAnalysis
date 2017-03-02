# -*- coding: utf-8 -*-
# coding=gbk
import re
import codecs

patGlossary = re.compile(r'^\W*(\w+)[=|]')

# 义原树
SememeList = []
# 义原词典
SememeDict = {}
# 义原的情感倾向
SememeEmotionOrientation = {}
# 基础词库
Glossary = {}

NegativeEmotionDict = {}
PositiveEmotionDict = {}

# 构造义原词典


def BuildSememeTree(file_path):
    with open(file_path) as f:
        for line in f:
            if line[:3] == codecs.BOM_UTF8:
                line = line[3:]
            term = line.strip().split()
            sememe = (term[1].split('|'))[0]
            if int(term[0]) == int(term[2]):
                SememeList.append({'sememe':sememe, 'parent':-1})
            else:
                SememeList.append({'sememe':sememe, 'parent':int(term[2])})
            SememeDict[sememe] = int(term[0])


def FindSememePath(sememe_id):
    if (0 <= sememe_id) and (sememe_id < len(SememeList)):
        return [sememe_id] + FindSememePath(SememeList[sememe_id]['parent'])
    else:
        return []

# 构造词典
def BuildGlossary(file_path):
    with open(file_path) as f:
        for line in f:
            if line[:3] == codecs.BOM_UTF8:
                line = line[3:]
            term = line.strip().split()
            # 成就 -
            #      |- V        fulfil|实现
            #     |- N        result|结果,desired|良,#succeed|成功
            theWord = term[0].decode('utf-8')
            if theWord in Glossary:
                if term[1] not in Glossary[theWord]:
                    Glossary[theWord][term[1]] = []
            else:
                Glossary[theWord] = {term[1]:[]}


            sememeList = (term[2].split(','))
            for s in sememeList:
                matchResult = patGlossary.match(s)
                if matchResult:
                    sememe_key = matchResult.group(1)
                    if sememe_key in SememeDict:
                        s_id = SememeDict[sememe_key]
                        s_SememeTreePath = FindSememePath(int(s_id))
                        Glossary[theWord][term[1]].append(s_SememeTreePath)


# 加载情感字典
def LoadEmotionDictionary(file_path, isPositiveEmotion = True):
    targetDict = PositiveEmotionDict
    if not isPositiveEmotion:
        targetDict = NegativeEmotionDict

    with open(file_path) as f:
        for line in f:
            if line[:3] == codecs.BOM_UTF8:
                line = line[3:]
            term = line.strip().decode('utf-8')
            if term in Glossary:
                targetDict[term] = Glossary[term]

# 统计义原下的情感词
def BuildSememeEmotionOrientation(emotionDict, value):
    for k in emotionDict:
        for attr in emotionDict[k]: #k.decode("utf-8")]:
            for sPath in emotionDict[k][attr]:
                for s in sPath:
                    if s in SememeEmotionOrientation:
                        SememeEmotionOrientation[s]['Ori'] += value
                        SememeEmotionOrientation[s]['Count'] += 1
                    else:
                        SememeEmotionOrientation[s] = {'Ori':value, 'Count': 1, 'Score':0}


# 计算义原的情感值
def CalculatorSememeEmotionScore():
    BuildSememeEmotionOrientation(NegativeEmotionDict, -1)
    BuildSememeEmotionOrientation(PositiveEmotionDict, 1)

    for k in SememeEmotionOrientation:
        SememeEmotionOrientation[k]['Score'] = SememeEmotionOrientation[k]['Ori']*1.0/SememeEmotionOrientation[k]['Count']


def BuildAll():
    pass



if __name__=='__main__':

    BuildSememeTree('./hownet/WHOLE.dat')

    BuildGlossary('./hownet/glossary.dat')
    # print Glossary['哀'.decode("utf-8")]

    LoadEmotionDictionary('./hownet/cn_negative_emotion.txt', False)
    print NegativeEmotionDict['哀'.decode("utf-8")]

    LoadEmotionDictionary('./hownet/cn_positive_emotion.txt')
    print PositiveEmotionDict['爱'.decode("utf-8")]

    # BuildSememeEmotionOrientation(NegativeEmotionDict, -1)
    # BuildSememeEmotionOrientation(PositiveEmotionDict, 1)

    CalculatorSememeEmotionScore()

    # for k in NegativeEmotionDict:
    #     for attr in NegativeEmotionDict[k]: #k.decode("utf-8")]:
    #         for sPath in NegativeEmotionDict[k][attr]:
    #             for s in sPath:
    #                 if s in SememeEmotionOrientation:
    #                     SememeEmotionOrientation[s]['Ori'] -= 1
    #                     SememeEmotionOrientation[s]['Count'] += 1
    #                 else:
    #                     SememeEmotionOrientation[s] = {'Ori':-1, 'Count': 1, 'Score':0}

    # # for k in SememeEmotionOrientation:
    # #     print str(k) + " " + str(SememeEmotionOrientation[k]['Ori']) + " " + str(SememeEmotionOrientation[k]['Count'])

    # for k in PositiveEmotionDict:
    #     for attr in PositiveEmotionDict[k]: #k.decode("utf-8")]:
    #         for sPath in PositiveEmotionDict[k][attr]:
    #             for s in sPath:
    #                 if s in SememeEmotionOrientation:
    #                     SememeEmotionOrientation[s]['Ori'] += 1
    #                     SememeEmotionOrientation[s]['Count'] += 1
    #                 else:
    #                     SememeEmotionOrientation[s] = {'Ori':1, 'Count': 1, 'Score':0}

    # for k in SememeEmotionOrientation:
    #     SememeEmotionOrientation[k]['Score'] = SememeEmotionOrientation[k]['Ori']*1.0/SememeEmotionOrientation[k]['Count']

    for k in SememeEmotionOrientation:
        print str(k) + " " + str(SememeEmotionOrientation[k]['Score'])



    # i = 0
    # with open('./hownet/modified_glossary_utf8.dat') as f:

    #     for line in f:
    #         if line[:3] == codecs.BOM_UTF8:
    #             line = line[3:]
    #         # print line.decode('string-escape').decode("utf-8")
    #         term = line.strip().split()
    #         print term
    #         print term[0]
    #         # print term[0].decode('string-escape').decode('utf-8')
    #         print term[0].decode('utf-8')
    #         # print int(term[0])
    #         print chardet.detect(term[0])
    #         print type(term[0]).__name__
    #         print isinstance(term[0], type('str'))
    #         print isinstance(term[0], type(u'str'))
    #         if i > 10:
    #             break
    #         else:
    #             i += 1
            # sememe = (term[1].split('|'))[0]
            # if int(term[0].encode('ascii')) == int(term[2].encode('ascii')):
            #     SememeList.append({'sememe':sememe, 'parent':-1})
            # else:
            #     SememeList.append({'sememe':sememe, 'parent':int(term[2].encode('ascii'))})
            # SememeDict[sememe] = int(term[0].encode('ascii'))

    # http://www.pythonclub.org/python-basic/codec
    # a = u'中午'
    # result = chardet.detect(a)
    # print result

    # if a == u'中午':
    #     print 'matched'
    # else:
    #     print 'not matched'

    # print a.encode('utf-8')

    # rawdata = open('./hownet/WHOLE_utf8.dat', "r").read()
    # result = chardet.detect(rawdata)
    # print result

    # rawdata = open('./hownet/glossary_utf8.dat', "r").read()
    # result = chardet.detect(rawdata)
    # print result

    # rawdata = open('./hownet/cn_negative_emotion_utf8.txt', "r").read()
    # result = chardet.detect(rawdata)
    # print result


    # print len(SememeList)
    # print SememeList[1617]
    # print SememeDict['focus']
    # # if 'focus' in SememeDict:
    # #     print "matched"
    # # else:
    # #     print "not matched"


    # print Glossary['2']
    # print Glossary['BP机'.encode('UTF-16LE')]
    # for k in Glossary.keys():
    #     print k
    #     print chardet.detect(k)
    #     print Glossary[k]
    # print Glossary['哀'.decode("utf-8")]


    # i = 0
    # with codecs.open('./hownet/cn_negative_emotion.txt', "r", "utf-8") as f:
    # with open('./hownet/modified_cn_negative_emotion_utf8.txt') as f:
    #     for l in f:
    #         if l in Glossary:
    #             print l + " matched"
    #             print Glossary[l]
    #         else:
    #             print l + " not matched"
            # if i > 10:
            #     break
            # else:
            #     i += 1


# with open('./hownet/WHOLE.dat') as wholeDoc:
#     data = wholeDoc.readline()
#     print data
#     term = data.strip().lstrip().split()
#     print term[0]
#     print term[1]
    # print data
    # result = pat_yiyuan.match(wholeDoc.readline())
    # if result:
    #     print "matched"
    #     print result.group()
    # else:
    #     print "not matched"