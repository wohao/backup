from suds.client import Client

string = "<?xml version='1.0' encoding='UTF-8'?><request><licenseCode>b176092352f76c33ce98d9cb2fc3e2a2</licenseCode><requestNo>E000000001</requestNo></request >"
url = "http://test-api.kbjcc.cc:13131/webservice/exam/services?wsdl"
client = Client(url)
result = client.service.examRequest(string)
print(result)
print(client)


# from suds.client import Client

# url = "http://192.168.0.31:81/ws_aps_sys.asmx?wsdl"
# client = Client(url)
# print(client)
# with open('result.txt',"w") as f:
# 	f.write(str(client))


# InPutDataHeader = "PACS9"
# InPutDataBody = "001,002,口腔,小王,2017-10-12 09:09:09,2017-10-12 09:09:09,检查结果，测试"
# result = client.service.ExceBusiness(InPutDataHeader=InPutDataHeader,InPutDataBody=InPutDataBody)
# print("111111111111"+result)
# import urllib.request

# s = urllib.request.urlopen("http://192.168.1.182:9001/getHisInfo?hisId=ZY00093787&type=1&departmentId=7017&doctorCode=012456")

# print(s)