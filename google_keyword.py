from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from nltk.corpus import stopwords
import re
import requests
import time
import cut_word
# 크롤링 봇 탐지 
# from selenium.webdriver.chrome.options import Options
# import chromedriver_autoinstaller
# import subprocess
# import shutil

# try:
#     shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
# except FileNotFoundError:
#     pass

# subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


# option = Options()
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
# try:
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
# except:
#     chromedriver_autoinstaller.install(True)
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
# driver.implicitly_wait(10)

def result(request):
    url=request

    #driver = webdriver.Chrome('chromedriver.exe')
    driver = webdriver.Firefox('')
    driver.get(url)
    driver.implicitly_wait(5)

    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0,500);")
    time.sleep(1.5)

    # 유튜브 팝업 닫기
    try:
        driver.find_element_by_css_selector("#dismiss-button > a").click()
    except:
        pass

        # 페이지 끝까지 스크롤
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(1.5)
    driver.execute_script("window.scrollTo(500,0);")

    # 대댓글 모두 열기
    buttons = driver.find_elements_by_css_selector("#more-replies > a")

    time.sleep(1.5)

    for button in buttons:
        button.send_keys(Keys.ENTER)
        time.sleep(1.5)
        button.click()

    time.sleep(1.5)

    # 정보 추출하기
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    id_list = soup.select("div#header-author > h3 > #author-text > span")
    comment_list = soup.select("yt-formatted-string#content-text")

    id_final = []
    comment_final = []

    for i in range(len(comment_list)):
        temp_id = id_list[i].text
        temp_id = temp_id.replace('\n', '')
        temp_id = temp_id.replace('\t', '')
        temp_id = temp_id.replace('    ', '')
        id_final.append(temp_id)

        temp_comment = comment_list[i].text
        temp_comment = temp_comment.replace('\n', '')
        temp_comment = temp_comment.replace('\t', '')
        temp_comment = temp_comment.replace('    ', '')
        comment_final.append(temp_comment)
    #
    # print(id_final)s
    # print(comment_final)

    return comment_final
    # f = open('origin.txt', 'w', encoding='UTF-8')
    #
    # for comment in comment_final:
    #     f.write(comment + '\n')
    #
    # f.close()
    #######################################################################################
    # file = open('origin.txt', 'r', encoding='UTF-8')
    # word_dict = {}
    #
    # keys = []
    # values = []
    # word_count = {}
    #
    # line = file.readline()
    # stop_words = set(stopwords.words('english'))
    # while line:
    #     sentence = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', ' ', line)
    #     sentence = sentence.lower()
    #     word_list = sentence.split()
    #     for word in word_list:
    #         if word not in stop_words:
    #             if word in word_count:
    #                 word_count[word] += 1
    #             else:
    #                 word_count[word] = 1
    #
    #     line = file.readline()
    #
    # sort_list = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # # print(sort_dict)
    # file.close()
    # f = open('sorted.txt', 'w', encoding='UTF-8')
    #
    # # print(type(sort_list[1]))
    # # print(sort_list[1])
    # for i in sort_list:
    #     string = str(i)
    #     string = string.strip("("")""'")
    #     string = string.replace(",", "")
    #     string = string.replace("'", "")
    #     f.write(string + '\n')
    #
    # f.close()
    #
    # return comment_final
    # 텍스트파일 정렬해서 sorted.txt로 붙여넣기
    ####################################################################
    # data = open('accounts/sorted.txt', 'r', encoding='UTF-8')
    # with open('accounts/happy.txt', encoding='UTF-8') as likef:
    #     like_words = likef.read().replace('\n', ' ')
    # with open('accounts/sad.txt', encoding='UTF-8') as dislikef:
    #     dislike_words = dislikef.read().replace('\n', ' ')
    # word_dicts = {}
    # lines = data.readlines()
    # keys = []
    # values = []
    #
    # for line in lines:
    #     (k, v) = line.split()
    #
    #     keys.append(k)
    #     int(v)
    #     values.append(v)
    #
    # word_dicts = {'key': keys, 'value': values, }
    #
    # like_num = 0
    # dislike_num = 0
    # for key in keys:
    #     if key in like_words:
    #         print(key + ' ' + 'is like')
    #         like_num += 1
    #     elif key in dislike_words:
    #         print(key + ' ' + 'is dislike')
    #         dislike_num += 1
    #     else:
    #         print(-1)
    # word_dict = {'id': id_final, 'comment': comment_final, 'like_num': like_num, 'dislike_num': dislike_num,
    #              'key': keys, 'value': values}
    # data.close

