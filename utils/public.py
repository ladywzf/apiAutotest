#作者:Administrator
#时间:2019/10/19
import sys
sys.path.append(r'C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\apiAutotest')
from xlutils import copy
import os
from apiAutotest.utils.operationJson import *
import xlrd
from apiAutotest.utils.operationExcel import *
import re
class public:
    # 获取文件路径
    def data_dir(self, data=None, filename=None):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, filename)

    # 创建目录
    def mkdir(self, foldername):
        path_dir ="E:\\"+"{0}".format(os.path.basename(os.path.dirname(os.path.dirname(__file__))))+"\\data\\{foldername}\\".format(foldername=foldername)
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        return path_dir

    # 创建文件
    def mkfile(self, folername, filename):
        path = self.mkdir(folername) + filename
        if not os.path.isfile(path):
            fd = open(path, mode="w", encoding="utf-8")
            fd.close()
        return path


    # 将token写入到文件中
    def writeToken(self, path, content):
        with open(path, "w") as f:
            f.write(content)
        f.close()

    # 将结果写入到excel中
    def writeResult(self, row, col, content, path):
        # col=excel_data.excel_data().get_result_col()
        work = xlrd.open_workbook(path)
        cwork = copy.copy(work)
        csheet = cwork.get_sheet(0)
        csheet.write(row, col, content)
        cwork.save(path)

    # 从token文件中获取token
    def get_token(self, path):
        with open(path, "r", encoding="utf-8") as f:
            token = f.read()
        f.close()
        return token

    # 不带token的头信息
    def getHeader(self):
        headers = {
            "content-type": "application/json",
            "Cookie": "noLoginLanguage=zh; oms_lang=zh; ems_lang=zh",
            #"Referer": "https://sdptest.shijicloud.com/open_source_pro/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        return headers

    # 带token的头信息
    def getHeader_token(self,path):
        headers = {
            "authorization": self.get_token(path),
            "content-type": "application/json",
            "Cookie": "noLoginLanguage=zh; oms_lang=zh; ems_lang=zh",
            #"Referer": "https://sdptest.shijicloud.com/open_source_pro/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        return headers

    # 获取url中的公共部分内容
    def get_public_url(self,path):
        public_url = operationJson().getReadJson(path)["public_url"]
        return public_url


    # 获取不带参的url
    def get_n_url(self, row, path, f):
        return self.get_public_url(path) + operationExcel.operationExcel().get_url_value(row, f)

    # 获取带一个参数的url
    def get_v_url(self, row, id, path, f):
        url = str(self.get_public_url(path) + operationExcel.operationExcel().get_url_value(row, f)).format(id)
        return url

    # 获取带两个参数的url
    def get_2v_url(self, row, id1, id2, path, f):
        url = str(self.get_public_url(path) + operationExcel.operationExcel().get_url_value(row, f)).format(id1,
                                                                                                            id2)
        return url
    #获取json文件中的参数
    def getData(self,row,f1,f2):
        l = []
        #print(type(operationJson().get_json_data(row, f1, f2)["data"]))
        data = operationJson().get_json_data(row, f1, f2)["data"]
        assertStr = operationJson().get_json_data(row, f1, f2)["assert"]
        for i in range(len(data)):
            l.append((data[i], assertStr[i]))
        return l

    """  
    # 灵活设置json文件中键对应的值的内容
    def set_key_val(self, row, f1, f2, l, li):
        jsonData = json.loads(operationJson().get_json_data(row, f1, f2))
        for i in range(0, len(l)):
            jsonData[l[i]] = li[i]
        return jsonData
        """
    #获取参数可自行输入的参数数据
    def getData001(self,row, f1, f2, lindex, lvalue):
        l = []
        data = operationJson().get_json_data(row, f1, f2)["data"]
        assertStr = operationJson().get_json_data(row, f1, f2)["assert"]
        for i in range(len(data)):
            for i in range(len([lindex])):
                data[lindex[i]]=lvalue[i]
            l.append((data[i], assertStr[i]))
            print(l[i])
        return l
    #正则表示式方式获取大括号内的内容
    def getContent(self,str):
        content=re.compile(r'[{](.*?)[}]', re.S)
        #print(re.findall(content, str))
        return re.findall(content, str)
    #获取字符串数组
    def getList(self,str):
        lr = str.split("{")
        lr = lr[1].split("}")
        lr = lr[0].split(",")
        return lr



