# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 10:46 AM
# @Author  : minghao.gao
# @FileName: mock_login_selenium.py
# @Software: PyCharm

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/login?from=home')
    browser.find_element_by_xpath("/html/body/div[@id='root']/div[@class='StyledBackground-sc-1duRon iFBgcJ']/div[@class='ModalContainer-sc-1duRon-3 tisQL']/div[@class='AnimateModal-sc-1duRon-4 bpBmPN']/div[@class='StyledContainer-sc-3JRwrF-1 eLdteR']/div[@class='main']/div[@class='switch-panel StyledSwitchPanel-sc-3JRwrF-5 gBlFBX']/div[@class='form-wrapper']/div[@class='StyledLogin-sc-2oZUsG bZrWhJ']/div[1]/div[@class='StyledInput-sc-3ksGSP iCbGBI']/div[@class='input']/input").send_keys('fake phoneNo.')
    browser.find_element_by_xpath("/html/body/div[@id='root']/div[@class='StyledBackground-sc-1duRon iFBgcJ']/div[@class='ModalContainer-sc-1duRon-3 tisQL']/div[@class='AnimateModal-sc-1duRon-4 bpBmPN']/div[@class='StyledContainer-sc-3JRwrF-1 eLdteR']/div[@class='main']/div[@class='switch-panel StyledSwitchPanel-sc-3JRwrF-5 gBlFBX']/div[@class='form-wrapper']/div[@class='StyledLogin-sc-2oZUsG bZrWhJ']/div[1]/div[@class='StyledInput-sc-3ksGSP dgMhGm']/div[@class='input']/input").send_keys('fake password')
    browser.find_element_by_xpath("/html/body/div[@id='root']/div[@class='StyledBackground-sc-1duRon iFBgcJ']/div[@class='ModalContainer-sc-1duRon-3 tisQL']/div[@class='AnimateModal-sc-1duRon-4 bpBmPN']/div[@class='StyledContainer-sc-3JRwrF-1 eLdteR']/div[@class='main']/div[@class='switch-panel StyledSwitchPanel-sc-3JRwrF-5 gBlFBX']/div[@class='form-wrapper']/div[@class='StyledLogin-sc-2oZUsG bZrWhJ']/div[1]/button[@class='sm-button submit sc-1n784rm-0 bcuuIb']").click()
    cookies = browser.get_cookies()
    print(cookies)
except Exception as e:
    print(e)
finally:
    browser.close()
