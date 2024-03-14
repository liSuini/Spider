import re
import requests

def main():
    schoolWebURL = 'http://219.226.127.250/a79.htm'
    user_account = "liangjiarui0428"
    user_password = "IMmc2500"

    while True:
        response = requests.get(schoolWebURL)

        pattern = re.compile('<title>(.*?)</title>', re.S)
        title = re.findall(pattern, response.text)
        title = title[0]

        if title == '注销页':
            pass
        else:
            schoolWebLoginURL = f"http://219.226.127.250:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C{user_account}&user_password={user_password}&wlan_user_ip=101.7.160.43&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2283&lang=zh"
            requests.get(schoolWebLoginURL)

if __name__ == "__main__":
    main()
