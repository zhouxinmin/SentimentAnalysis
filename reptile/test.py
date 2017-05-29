# ! /usr/bin/env python
# -*- coding: utf-8 --
# ---------------------------
# @Time    : 2017/4/15 10:37
# @Site    : 
# @File    : test.py
# @Author  : zhouxinmin
# @Email   : 1141210649@qq.com
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import re

# url = 'https://movie.douban.com/subject/1292213/comments?status=P'
urls = ['https://movie.douban.com/review/best/?start={}'.format(str(i)) for i in range(0, 100, 20)]
for single_url in urls:
    wb_data = requests.get(single_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # evaluates = soup.select('div[class="short_content"]')
    pattern_star = re.compile(r'<span class = "allstar\d+" title = "(.+)"></span>')
    print pattern_star
    for item in soup.find_all('div', class_='item'):  # 找到每一个影片项
        star = re.findall(pattern_star, item)[0]
    # print soup
        print star
