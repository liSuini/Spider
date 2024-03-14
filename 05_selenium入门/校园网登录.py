# _*_ coding : utf-8 _*_

import re    # 正则表达式，用于匹配字符
import requests    # 用于向目标网站发送请求


schoolWebURL = 'http://219.226.127.250/a79.htm'    # 这行是你需要根据自己的情况修改的地方


while(True):
    response = requests.get(schoolWebURL)

    # 正则表达式，匹配<title>标签中的内容
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.findall(pattern, response.text)
    title = title[0]    # 将格式转为字符串

    if title == '注销页':    # 根据上面的分析填入相应的字符
        pass
    else:
        # 使用GET方式登录校园网
        schoolWebLoginURL = "http://219.226.127.250:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2Climingwu0426&user_password=EYgg9433&wlan_user_ip=101.7.160.43&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2283&lang=zh"
        requests.get(schoolWebLoginURL)