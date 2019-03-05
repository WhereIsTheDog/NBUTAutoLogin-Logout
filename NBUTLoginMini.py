#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:19:28 2019

@author: nickfu
"""

import requests
import time

def login(user, pwd):
    NetState = "%25E5%25A4%2596%25E7%25BD%2591"
    header = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    requestData = "wlanuserip%253dc6852957b34b40aec22acd76b8046626%2526wlanacname%253d8e98b113152ff1af%2526ssid%253d%2526nasip%253d4013a1c6a367f06166df141778c1eeb4%2526snmpagentip%253d%2526mac%253d2e125bd61901e14c8a41c07d38ee884e%2526t%253dwireless-v2%2526url%253dd91522d922cf13731f7d10614e27a19fc017a1765de201c2%2526apmac%253d%2526nasid%253d8e98b113152ff1af%2526vid%253debe51f505138092c%2526port%253d9d75df5fa14a33ad%2526nasportid%253d29864c3e14289b8596094d41130e35e28f068ebb906d5b6431f859c9ccf895909914da0cad0b2c0a"
    postData = "userId=" + user + "&password=" + pwd + "&service=" + NetState + "&queryString=" + requestData + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
    responseRes = requests.post("http://10.23.4.165/eportal/InterFace.do?method=login", data = postData, headers = header)
    if len(f"{responseRes.text}") == 220:
        return True
    else:
        return False

def logout():
    responseRes = requests.post("http://10.23.4.165/eportal/InterFace.do?method=logout")
    if "success" in (f"{responseRes.text}"):
        return True
    else:
        return False

if __name__ == '__main__':
    print("NBUT auto login & logout is running.")
    user = "17406040116"  #账号
    pwd = "210318"  #密码
    sleeptime = 600 #休眠时间 600秒
    if login(user, pwd) == False:
        logout()
    while (True):
        login(user, pwd)
        time.sleep(sleeptime)
        logout()
        time.sleep(1)