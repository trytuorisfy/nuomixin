# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import os
# import xlwt

browser = webdriver.PhantomJS()
# browser = webdriver.Chrome()
WAIT = WebDriverWait(browser, 10)

count = 0
txtName = ''
def next_page():
    try:
        # print('获取下一页数据')
        next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                          '#pb_next')))
        next_btn.click()
        WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                               '#pb_next')))
        get_source()
    except TimeoutException:
        # browser.refresh()
        # return next_page(page_num)
        return


def get_page(url):
    try:
        print('开始访问')
        browser.get(url)
        get_source()
    except TimeoutException:
        # browser.refresh()
        # return next_page(page_num)
        return

def save_to_txt(soup):
    title = soup.find(id='nr_title').get_text() + '\r\n'
    print(title)
    with open(txtName, 'a+', encoding='utf-8', errors='ignore') as f:
        f.write(title)  # 文件的写操作
    
    content = soup.find_all(id="nr1")
    # print(content)

    #将小说内容写入txt文本文档
    for i in content:
        new_str = i.get_text('<br>', '\n')
        str = re.sub('<br>', '\r\n', new_str)  # 将文档中的<br>标签替换为换行符
        with open(txtName, 'a+', encoding='utf-8', errors='ignore') as f:
            f.write(str)  # 文件的写操作

    next_page()

def get_source():
    WAIT.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#nr1')))



    html = browser.page_source
    
    soup = BeautifulSoup(html, 'lxml')
    # f.close()
    global count 
    global txtName 
    if count == 0:       
        txtName = soup.h1.get_text() + '.txt'
    count += 1
    save_to_txt(soup)


def main():
    try:
        url = 'https://m.meiguixs.net/html/120/120071/43850964.shtml'
        get_page(url)
    finally:
        browser.close()

if __name__ == '__main__':
   
    main()
    print('结束')
