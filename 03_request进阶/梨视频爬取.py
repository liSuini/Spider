import requests
import os
if not os.path.exists("梨视频"):
    os.mkdir("梨视频")
contId = "https://pearvideo.com/video_1777816".split("_")[1]
url = "https://pearvideo.com/videoStatus.jsp?contId=1777816&mrd=0.6281112342338115"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Referer": "https://pearvideo.com/video_1777816"
}
resp = requests.get(url=url,headers=headers)
systemtime = resp.json()['systemTime']
src_url= resp.json()['videoInfo']['videos']["srcUrl"]
src_url = src_url.replace(systemtime,f"cont-{contId}")
print(resp.json()['systemTime'])
print(resp.json()['videoInfo']['videos']["srcUrl"])
print(src_url)
resp2 = requests.get(url=src_url,headers=headers)
with open("梨视频/"+contId+".mp4","wb") as fp:
    fp.write(resp2.content)

resp.close()
resp2.close()

#
# https://video.pearvideo.com/mp4/short/20230131/cont-1777816-71080544-hd.mp4
# https://video.pearvideo.com/mp4/short/20230131/1675154555523-71080544-hd.mp4



