#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:00:56 2019

@author: nickfu
"""

import urllib.request
import requests
from bs4 import BeautifulSoup
import re


url = "http://10.23.4.165"
user = "17406040116"  #账号
pwd = "210318"  #密码
NetState = "%25E5%25A4%2596%25E7%25BD%2591"
#网络状态 ＝ “%25E5%2586%2585%25E7%25BD%2591”/*内网*/
#网络状态 ＝ “%25E5%25A4%2596%25E7%25BD%2591”/*外网*/
header = {
#        "Host": "10.23.4.165",
#        "Connection": "keep-alive",
#        "Content-Length": "645",
#        "Origin": "http://10.23.4.165",
#        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#        "Accept": "*/*",
#        "Referer": "http://10.23.4.165/eportal/index.jsp?wlanuserip=0d58d5a385490e7c63abe633c3236cc0&wlanacname=8e98b113152ff1af&ssid=&nasip=4013a1c6a367f06166df141778c1eeb4&snmpagentip=&mac=d8d542c70c61dec85de984fecd5d918c&t=wireless-v2&url=d91522d922cf13731f7d10614e27a19fc017a1765de201c2&apmac=&nasid=8e98b113152ff1af&vid=ba1754a80a3d4bb3&port=4a540cee214e86cf&nasportid=29864c3e14289b8596094d41130e35e21fea8d519f53d0d6576a2aea6249d16901898b4963f54257",
#        "Accept-Language": "zh-CN,zh;q=0.9"
}


#上线部分
response = urllib.request.urlopen(url)  #打开网页
star = response.read()   #读取网页
soup = BeautifulSoup(star, 'html.parser')  #解析网页
url2 = (re.search(r'\'(.+?)\'', str(soup), re.M|re.I)).group(1)  #获取第二次的网页链接
#重复操作 解析
response2 = urllib.request.urlopen(url2)
star2 = response2.read()
soup2 = BeautifulSoup(star2, 'html.parser')
requestData = (re.search(r'\?(.+?)\'', str(soup), re.M|re.I)).group(1)
requestData = requestData.replace("=", "%253d")  #把“=”进行两次Url编码并替换
requestData = requestData.replace("&", "%2526")

postData = "userId=" + user + "&password=" + pwd + "&service=" + NetState + "&queryString=" + requestData + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"

responseRes = requests.post("http://10.23.4.165/eportal/InterFace.do?method=login", data = postData, headers = header)
print(f"statusCode = {responseRes.status_code}")
print(f"text = {responseRes.text}")


#下线部分
returnText = f"{responseRes.text}"
userIndex = (re.search(r'"userIndex\":"(.+?)"', str(returnText), re.M|re.I)).group(1)
responseRes = requests.post("http://10.23.4.165/eportal/InterFace.do?method=logout", data = "userIndex="+userIndex)