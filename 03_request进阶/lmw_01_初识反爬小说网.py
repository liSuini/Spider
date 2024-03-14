import requests

if __name__ == '__main__':
    # 创建 session 会话对象
    session = requests.session()
    url = "https://passport.17k.com/ck/user/login"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    data ={
        "loginName":"15110462861",
        "password":"lmw.19990228"
    }
    session.post(url=url, data=data)
    resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
    print(resp.json())
