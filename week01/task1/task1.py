# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 1:13 PM
# @Author  : minghao.gao
# @FileName: task1.py
# @Software: PyCharm

"""
作业一：

安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
cookie = '_csrf=0127f6e0868b5fc20db47c6243f00c5aab779439d8fa96be903b52e9f5e76ed1; uuid=ACD18D80CBF211EAA86FA7C86A03EB65DD46CAD344574D4399BB769326055DA4; uuid_n_v=v1; Pycharm-7fee7579=8abd7771-bdf6-4dc1-9db5-563f95eb202b'
header = {'user-agent': user_agent,'cookie':cookie}


url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=header)
bs_info = bs(response.text, 'html.parser')
movie_details = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    name = tags.find('span', attrs={'class': 'name'}).text
    scores = tags.find('span', attrs={'class': 'score channel-detail-orange'})
    if scores is not None:
        integer = scores.find('i', attrs={'class': 'integer'}).text
        fraction = scores.find('i', attrs={'class': 'fraction'}).text
        movie_score = integer+fraction
    else:
        movie_score = '暂无评分'
    for divs in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        for spans in divs.find_all('span', attrs={'class': 'hover-tag'}):
            if spans.text == '类型:':
                spans.replace_with('')
                movie_type = divs.text.replace(' ', '').strip()
    movie_detail = [name, movie_score, movie_type]
    movie_details.append(movie_detail)
print(movie_details)
movie = pd.DataFrame(data=movie_details[:10])
movie.to_csv('./movie.csv', encoding='utf-8', index=False, header=['影片名称', '评分', '种类'])
