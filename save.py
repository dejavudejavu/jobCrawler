# 导入Flask类
from flask import Flask,make_response,send_file, send_from_directory
from flask import render_template,request,jsonify
import json
import requests,re
from bs4 import BeautifulSoup
import jieba
from fake_useragent import UserAgent
import random
import urllib
from lxml import etree
import time
from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import http.client
import os

http.client._MAXLINE=655360
# 实例化，可视为固定格式
app = Flask(__name__)

# route()方法用于设定路由；类似spring路由配置
@app.route('/')
def hello():
    return render_template('/web/html/index.html')
@app.route('/ajaxtest')
def hello_world():
    # stop = open("stopword.txt", "r+", encoding='utf-8')
    # stopword = stop.read().split("\n")
    # return str(stopword)
    key = request.values.get("key")
    city = request.values.get("city")
    min = request.values.get("min")
    max = request.values.get("max")
    field = request.values.get("field")

    num=0
    curPage=0

    count = {}

    user_Agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
    ]
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__uuid=1600531008274.42; __s_bid=d0fb4ab7c069354128d606f74ae2dce6563a; fe_se=-1601348106674; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1600922425,1601131880,1601348107,1601425864; JSESSIONID=6545DAC4CD5A0DD0E3B044BF64C63F59; __tlog=1601348106924.83%7C00000000%7CR000000075%7Cs_o_001%7Cs_o_001; __session_seq=8; __uv_seq=6; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1601426678',
    'Host': 'www.liepin.com',
    'Referer': 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=',
    'Upgrade-Insecure-Requests': '1'
    # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63
    }

    #headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    key = request.values.get("key")
    city = request.values.get("city")
    min = request.values.get("min")
    max = request.values.get("max")
    field = request.values.get("field")

    num=0
    curPage=0

    count = {}

    # while num<80:
    time.sleep(0.1)  
    ua = random.choice(user_Agent)
    headers['User_Agent'] = ua
    url='https://www.liepin.com/zhaopin/?key='+key
    # url='https://www.liepin.com/zhaopin/?key='+key+'&curPage='+str(curPage)+'&salary='+min+'%24'+max+'&industries='+field+'&dqs='+city
    curPage+=1
    response=requests.get(url,headers=headers)
    content=response.content.decode('utf-8')

    soup = BeautifulSoup(content,"html.parser")
    for tag in soup.find_all('div',class_="job-info"):
        jobUrl=tag.find('a').get('href')
        if jobUrl.startswith('/a')==True:
            jobUrl='https://www.liepin.com'+jobUrl
        num+=1
        print(jobUrl,num)
        ua = random.choice(user_Agent)
        headers['User_Agent'] = ua
        time.sleep(0.1)
        response=requests.get(jobUrl,headers=headers)
        content=response.content.decode('utf-8')
        soup = BeautifulSoup(content,"html.parser")
        for tag in soup.find_all('div',class_=['job-item main-message job-description','job-main job-description main-message']):
            content=tag.find('div',class_='content content-word').get_text()
        # with open('E:\\求职app\\test.txt', 'a+') as file_object:
        #     file_object.write(str(num)+content.replace(u'\xa0', u''))
        words = jieba.lcut(content)
        #print(words,end='')
        #获取停用词表
        stop = open("stopword.txt", "r+", encoding='utf-8')
        stopword = stop.read().split("\n")
        for word in words:            #  使用 for 循环遍历每个词语并统计个数
            if len(word) < 2:          # 排除单个字的干扰，使得输出结果为词语
                continue
            else:
                count[word] = count.get(word, 0) + 1    #如果字典里键为 word 的值存在，则返回键的值并加一，如果不存在键word，则返回0再加上1
        # 建立无关词语列表
        for key in list(count.keys()):     # 遍历字典的所有键，即所有word
            if key in stopword:
                del count[key]                  #  删除字典中键为无关词语的键值对
#       time.sleep(random.random())
    mask = np.array(image.open("无标题.jpg"))
    wordcloud = WordCloud(
    background_color='rgb(179, 255, 255)',
    mask=mask,
    # font_path = "C:\\Windows\\Fonts\\msyh.ttc"
    ).generate_from_frequencies(count)
    image_produce = wordcloud.to_image()
    image_produce.show()

    


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="127.0.0.1", port=8080)


