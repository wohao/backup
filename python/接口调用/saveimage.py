'''
循环调用医真接口
1.获取token
2.组装数据
3.requests
'''
import requests
import json

 

tokenurl = 'https://192.168.2.130/amol-back/oauth/token?client_id=amol_client_mbox&client_secret=amol_secret_mbox&grant_type=password&username=mbox&password=123456'

response = requests.get(tokenurl,verify=False).json()
print(response)
token = response["access_token"]
print(token)
imageurl = 'https://192.168.2.130/amol-back/webs/saveImage?access_token={}&lang=zh_CN'.format(token)
print(imageurl)
headers = {'content-type': 'application/json'}
datas={
"ae":"iMAGES108",
"age":"68",
"checkNo":"1710110031",
"checkPart":"",
"dataStatus":"ONLINE",
"hospitalFk":"100651",
"imageNo":"p1710110031",
"imageNum":"1",
"imagePathOut":"Storage/ZG/610113/100651/RF/2017/10/11/20171011.11.55_21",
"imageSize":"698091",
"modality":"RF",
"patientName":"王解放_1710110031",
"serialNumber":"C5458834157BF126386D8AF9F3F6613A",
"sex":"M",
"storeDateTime":"2017-10-11 14:08:09",
"studyDateTime":"2017-10-11 09:00:05",
"studyUid":"20171011.11.55"
}
seriesDatas=[{
"imageNumber":"1",
"imageSize":"698091",
"seriesInstanceUID":"20171011.11.56",
"seriesName":"001_Barium%20%20Gaster",
"seriesPath":"Storage/ZG/610113/100651/RF/2017/10/11/20171011.11.55_21/001_000001_33766"}]
post_response = requests.post(imageurl,data=datas,verify=False)
print(post_response.text)
# print(token["access_token"])
# for k,v in token.items():
# 	print(k,v)
# print(type(token))
# print(response.json())

