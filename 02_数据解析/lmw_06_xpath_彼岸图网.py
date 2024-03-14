import requests
from lxml import etree
import os

if __name__ == '__main__':
    url = "https://pic.netbian.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    if not os.path.exists("彼岸图网"):
        os.mkdir("彼岸图网")

    resp_1 = requests.get(url=url,headers=headers)
    resp_1.encoding = "gbk"


    et_1 = etree.HTML(resp_1.text)

    # 创建每个子目录的字典索引
    dir_dict = {}
    a_lst = et_1.xpath('//*[@id="main"]/div[2]/a')
    for a in a_lst:
        name = a.xpath('./@title')[0].lstrip('4K')
        href = url+a.xpath('./@href')[0].lstrip('/')
        dir_dict[name] = href
    print("可以爬取的图片类型有：")
    print(dir_dict.keys())

    # 访问图片类型
    type= input("请输入要爬取的类型：")
    resp_2 = requests.get(url= dir_dict[type],headers=headers)
    resp_2.encoding = "gbk"

    if not os.path.exists('彼岸图网/'+type):
        os.mkdir('彼岸图网/'+type)

    et_2 =etree.HTML(resp_2.text)



    li_lst = et_2.xpath('//*[@id="main"]/div[3]/ul/li')
    #                 //*[@id="main"]/div[3]/ul/li[1]/a/img
    for li in li_lst:
        pic_name = li.xpath('.//text()')[0]
        pic_src = url +li.xpath('./a/@href')[0].lstrip('/')
        resp_3 = requests.get(url=pic_src,headers=headers)
        resp_3.encoding = "gbk"
        et_3 = etree.HTML(resp_3.text)
        img_url =url + et_3.xpath('//*[@id="img"]/img/@src')[0].lstrip('/')
        resp_4 = requests.get(url = img_url,headers=headers)
        with open('彼岸图网/'+type+"/"+pic_name+".jpg","wb") as f:
            f.write(resp_4.content)
        print(pic_name+"\t下载完成！！")

    max_page = int(et_2.xpath('//*[@id="main"]/div[4]/a[8]/text()')[0])
    page_num = 1
    while 1:
        if int(input(f"共有{max_page}页内容！！！是否爬取下一页内容(是：1 ，否：0):")):
            page_num +=1
            resp_2 = requests.get(url=f"{dir_dict[type]}/index_{page_num}.html", headers=headers)
            resp_2.encoding = "gbk"
            et_2 = etree.HTML(resp_2.text)
            li_lst = et_2.xpath('//*[@id="main"]/div[3]/ul/li')
            for li in li_lst:
                pic_name = li.xpath('.//text()')[0]
                pic_src = url + li.xpath('./a/@href')[0].lstrip('/')
                resp_3 = requests.get(url=pic_src, headers=headers)
                resp_3.encoding = "gbk"
                et_3 = etree.HTML(resp_3.text)
                img_url = url + et_3.xpath('//*[@id="img"]/img/@src')[0].lstrip('/')
                resp_4 = requests.get(url=img_url, headers=headers)
                with open('彼岸图网/' + type + "/" + pic_name + ".jpg", "wb") as f:
                    f.write(resp_4.content)
                resp_3.close()
                resp_4.close()
                print(pic_name + "\t下载完成！！")
            print("\n")
        else:
            break
        # print(pic_src,pic_name)

    print("over！！！！")
    #
    resp_1.close()
    resp_2.close()


