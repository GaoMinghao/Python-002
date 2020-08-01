# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 08:46 AM
# @Author  : minghao.gao
# @FileName: mock_login_selenium.py
# @Software: PyCharm
# 不是很清楚哪个部分校验不通过导致403返回，希望助教看到我这句话可以教我下，thanks ～ ：）

import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    'Refer': 'https://shimo.im/login?from=home'
}
form_data = 'mobile=%2B8617601294791&password=123456'
pre_login = "https://shimo.im/login?from=home"
login = "https://shimo.im/lizard-api/auth/password/login"
with requests.Session() as s:
    s.get(pre_login, headers=headers)
    response = s.post(login, data=form_data, headers=headers, cookies=s.cookies)
    print(response)
