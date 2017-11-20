import requests
import json
import re
import time

headers = {"authorization":"F20D6B93-51D4-C9E1-0CFC-2E63E65B1D33",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
'Connection': 'Keep-Alive',
'Referer':"https://wx.xiaomiquan.com/dweb/"}

timelist = ["2017-09-12T19%3A20%3A48.616%2B0800","2017-05-05T16%3A09%3A01.818%2B0800","2017-03-07T00%3A50%3A09.817%2B0800","2017-02-22T21%3A31%3A33.599%2B0800"]
#tests = requests.options("https://api.xiaomiquan.com/v1.8/groups/2421112121/topics?scope=by_owner&count=20&end_time=2017-11-17T15%3A50%3A05.817%2B0800",headers=headers)
for i in range(len(timelist)):

	test = requests.get("https://api.xiaomiquan.com/v1.8/groups/2421112121/topics?scope=digests&count=20&end_time={}".format(timelist[i]),headers=headers)
	text = test.json()
	strtext = json.dumps(text,ensure_ascii=False)
	# #result = re.findall(strtext,retext)

	#print(strtext)


	for k ,v in text.items():
		if isinstance(v,dict):
			for ke,va in v.items():
				#print(type(va))
				for lists in va:
					# print(type(lists))
					# print(lists)
					for key ,val in lists.items():
						if key == "talk":
							for keys ,valu in val.items():
								if keys == "text":
									print(valu)
									with open("test1.txt","a",encoding="utf-8") as f:
										f.write(valu+"\n")
						

# 			#print(ke,va)

