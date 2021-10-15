from apiAutotest.base.method import *
import unittest
from apiAutotest.utils.excel_data import excel_data as e
from apiAutotest.utils.public import *


obj = method()
excel_data = e()
p = public()
fileName=os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
# 获取实际结果列数
r_col = excel_data.get_result_col()
# 获取响应时间列数
t_col = excel_data.get_time_col()
f_purl = "public_url.json"
f_param = "requestData.json"
f_url = "data.xls"
f_token = "token"
p_purl = p.mkfile(fileName, f_purl)
p_param = p.mkfile(fileName, f_param)
p_url = p.mkfile(fileName, f_url)
p_token = p.mkfile(fileName, f_token)

class Test(unittest.TestCase):

    def write2excel(self,r,row,f):
        p.writeResult(row, r_col, "pass",f)
        p.writeResult(row, t_col, r.elapsed.total_seconds(),f)
    global data1
    global assertStr1
    #global t1json
    ltuple1=p.getData(1, p_purl, p_url)
    for i in range(len(ltuple1)):
        (data1, assertStr1)=ltuple1[i]
        def test_001(self):
            global t1json
            print(data1)
            print(type(data1))
            #登陆系统
            r=obj.post(1,p_purl,data1,p_url)
            lstr = p.getContent(json.dumps(assertStr1))
            # 将返回结果分割成列表
            lr = p.getList(r.text)
            # 去掉断言数据中的空格
            str = lstr[0]
            str1 = str.replace(" ", "")
            self.assertIn(str1,lr)
            print(r.json())
            if r.json()["data"]!=None:
                p.writeToken(p_token, r.json()["data"]["token"])
            t1json=r.json()
            self.write2excel(r,1,p_url)

    ltuple2 = p.getData(2, p_param, p_url)
    global data2
    global assertStr2
    #global t2json
    for i in range(len(ltuple2)):
        (data2, assertStr2) = ltuple2[i]
        def test_002(self):
            global t2json
            r = obj.post_t(2, p_token, p_purl, data2, p_url)
            # r=self.obj.post_token(2)
            #提取大括号内seertStr的内容，返回一个只有一个元素的列表
            lstr=p.getContent(json.dumps(assertStr2))
            #将返回结果分割成列表
            lr=p.getList(r.text)
            #去掉断言数据中的空格
            str=lstr[0]
            str1=str.replace(" ","")
            self.assertIn(str1,lr)
            t2json = r.json()
            self.write2excel(r, 2, p_url)
    def test_003(self):
        global t1json
        global t2json
        print("88888888888888888888888888888888888")
        print(t2json)
        print(t1json)
        pass
        #print(Test.__dict__["l2"][1])
    """ def test_002(self):
        # 加载菜单
        r = self.obj.get_t(2, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 2, self.p_url)
        #个人信息查询
        r = self.obj.get_t(3, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 3, self.p_url)
        #个人信息保存
        r = self.obj.post_t(4, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 4, self.p_url)
        #查询行业类别
        r = self.obj.get_t(5, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 5, self.p_url)
        if len(r.json()["data"]) > 0:
            industry_useflag = r.json()["data"][0]["industry_useflag"]
            id = r.json()["data"][0]["id"]
            if industry_useflag =="1":
                r = self.obj.get_v(7, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                if r.json()["status"]==202000061:
                    print("存在关联数据，不能被禁用")
                else:
                    self.write2excel(r, 7, self.p_url)
                #r = self.obj.get_v(6, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                #self.write2excel(r, 6, self.p_url)
            else:
                r = self.obj.get_v(6, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 6, self.p_url)
                r = self.obj.get_v(7, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 7, self.p_url)
        #获取可选择语言
        r = self.obj.get_t(8, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 8, self.p_url)
        # 查询币种设置
        r = self.obj.get_t(9, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 9, self.p_url)
        total = r.json()["data"]["total"]
        if total > 0:
            id = r.json()["data"]["rows"][0]["id"]
            name = r.json()["data"]["rows"][0]["name"]
            useFlag = r.json()["data"]["rows"][0]["useFlag"]
            code = r.json()["data"]["rows"][0]["code"]
            # 编辑币种
            r = self.obj.get_v(10, id, self.p_token,self.p_purl,self.p_param,self.p_url)
            self.write2excel(r, 10, self.p_url)
            # 保存币种
            l = []
            li = []
            l.append("name")
            li.append(name)
            l.append("code")
            li.append(code)
            l.append("useFlag")
            li.append(useFlag)
            l.append("id")
            li.append(id)
            r = self.obj.post_c(11, self.p_token,self.p_purl,self.p_param,self.p_url, l, li)
            self.write2excel(r, 11, self.p_url)
            if useFlag=="1":
                r=self.obj.get_v(13,id,self.p_token,self.p_purl,self.p_param,self.p_url)
                if r.json()["status"]==202000062:
                    print("已被引用，不能被禁用")
                else:
                    self.write2excel(r,13,self.p_url)
                r = self.obj.get_v(12, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 12, self.p_url)
            else:
                r = self.obj.get_v(12, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 12, self.p_url)
                r = self.obj.get_v(13, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 13, self.p_url)
        # 获取币种树
        r = self.obj.get_t(14, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 14, self.p_url)
        id=r.json()["data"][0]["key"]
        #获取单个行业多语言
        r=self.obj.get_v(15,id,self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r,15,self.p_url)
        # 系统语言查询
        r = self.obj.get_t(16, self.p_token,self.p_purl,self.p_param,self.p_url)
        self.write2excel(r, 16, self.p_url)
        if r.json()["data"]["total"] > 0:
            id = r.json()["data"]["rows"][0]["id"]
            name = r.json()["data"]["rows"][0]["name"]
            isoCode = r.json()["data"]["rows"][0]["isoCode"]
            # 系统语言编辑
            r = self.obj.get_v(17, id, self.p_token,self.p_purl,self.p_param,self.p_url)
            self.write2excel(r, 17, self.p_url)
            useFlag = r.json()["data"]["useFlag"]
            # 系统语言保存
            l = []
            li = []
            l.append("id")
            li.append(id)
            l.append("name")
            li.append(name)
            l.append("isoCode")
            li.append(isoCode)
            r = self.obj.post_c(18, self.p_token,self.p_purl,self.p_param,self.p_url, l, li)
            self.write2excel(r, 18, self.p_url)
            if useFlag =="0":
                r = self.obj.get_v(19, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 19, self.p_url)
                r = self.obj.get_v(20, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 20, self.p_url)
            else:
                r = self.obj.get_v(20, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                if r.json()["status"]==202000056:
                    print("被引用，不能被禁用")
                else:
                    self.write2excel(r, 20, self.p_url)
                r = self.obj.get_v(19, id, self.p_token,self.p_purl,self.p_param,self.p_url)
                self.write2excel(r, 19, self.p_url)
   """
if __name__ == '__main__':
    unittest.main()