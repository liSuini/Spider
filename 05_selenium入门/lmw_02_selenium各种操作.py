import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


web = Chrome()
def get():
    web.get("http://www.lagou.com")
    time.sleep(1)
    x = web.find_element("xpath",value='//*[@id="cboxClose"]')
    # 在selenium 中可以直接复制xpath路径，不需要考虑源代码有没有
    x.click()
    time.sleep(1)

    # 搜索框输入python 点击搜索
    # 通过回车键实现搜索
    web.find_element("xpath",'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
    time.sleep(2)
    div_list = web.find_elements("xpath",'//*[@id="jobList"]/div[1]/div')
    for div in div_list:
        a = div.find_element("xpath",'.//a')
        a.click()
        # 此时在浏览器这边已经打开了新的页面
        # 但是对于selenium 而言，此时他的视角仍然在首页
        # 所以，需要将selenium的视角调整到新开的页面
        # 切换窗口
        web.switch_to.window(web.window_handles[-1])
        job = web.find_element('xpath','//*[@id="job_detail"]/dd[2]')
        print(job.text)
        web.close()
        web.switch_to.window(web.window_handles[0])
        time.sleep(1)

    time.sleep(5)
    web.quit()

if __name__ == '__main__':
    get()