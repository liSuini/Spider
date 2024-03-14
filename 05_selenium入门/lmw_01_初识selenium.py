# selenium可以自动打开一个浏览器
# 输入网址
# 能从页面中提取信息
# 先确定是打开哪个浏览器 -> Chrome
import time

from  selenium.webdriver import Chrome

# 创建浏览器对象
# executable_path：指定浏览器驱动路径
web = Chrome()

url = "http://www.baidu.com"

web.get(url)

t = web.title
print(t)


