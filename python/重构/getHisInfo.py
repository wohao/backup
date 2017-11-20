import re
import pymysql
import socket
import json
from collections import OrderedDict

his_table={
"hisId" :"hisId",
"accessionNo":"accessionNo",
"checkPartName":"checkPartName",
"checkItemName":"checkItemName",
"patientName":"patientName",
"sex":"sex",
"birthday":"birthday",
"admId":"admId",
"admIdIss":"admIdIss",
"extNo":"extNo"
}
def GetQueryValue(sQueryContent,sKey):
	pattern = re.compile(r'{}=(.*?)&'.format(sKey))
	return re.search(pattern,sQueryContent).group(1)

def searchdata(sQueryUrl):
	hisId = GetQueryValue(sQueryUrl,"hisId")
	Type = GetQueryValue(sQueryUrl,"type")
	conn = pymysql.connect(host="192.168.1.189",port=3306,user="root",passwd="12345",db="his",charset='utf8',cursorclass=pymysql.cursors.DictCursor)
	cursor = conn.cursor()
	#cursor.execute("select * from pacs_gethisinfo group by modalityName")
	cursor.execute("select * from pacs_gethisinfo  where accessionNo ='{}' or hisId = '{}'".format(hisId,hisId))

	#datas = cursor.fetchone()
	datas = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()

	rJsonData={}
	rExanitems={}
	for i in datas:
		for yizhen_name,his_name in his_table.items():
			for name ,value in i.items():
				if name == his_name:
					rJsonData[yizhen_name]=value
				    #print(rJsonData[yizhen_name])
				if name == "admIdIss":
					if value == "住院号":
						rJsonData[name]=0

				if name == "checkItemName":
					rExanitems["itemName"]=value

				if name == "extNo":
					rExanitems["extNo"]= value

	btable=[rExanitems]
	rJsonData["checkItemName"]=btable
	ctable = [rJsonData]
	#print(c)
	
	#print(a)
	length = len(datas)
	sResultDetail="共查询到 {} 条记录".format(length)
	rJsonObject={}
	rJsonObject["resultCode"]=0
	rJsonObject["resultDatas"]=ctable
	rJsonObject["resultDetail"]=sResultDetail
	#print(rJsonObject)
	#returndata = json.dumps(rJsonObject)
	print(rJsonObject)

	return rJsonObject


if __name__ == '__main__':
	
	print("你好，世界！")
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(("192.168.1.40",9000))
	s.listen(100)
	
	conn , addr = s.accept()
	request = conn.recv(1024)
	print("Received from {d[0]}:{d[1]}".format(d=addr))
	request = str(request,encoding="utf-8")
	method = request.split(' ')[0]
	src  = request.split(' ')[1]
	print(method,src)
	ruesult = searchdata(src)
	
	#ss = json.dumps(ruesult).encode('utf-8')
	#s = ruesult.encode('utf-8')
	# print(ss)
	# conn.send(ss)
	conn.send(bytes('HTTP/1.1 200 OK\r\n\r\n<html><body>{}</body></html>'.format(ruesult),'utf-8'))
	conn.close()
