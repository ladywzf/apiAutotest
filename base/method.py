#作者:Administrator
#时间:2019/10/20
from apiAutotest.utils import operationExcel
from apiAutotest.utils.operationJson import operationJson as op
from apiAutotest.utils.public import *
import requests
import json
class method:
    def __init__(self):
        self.excel=operationExcel.operationExcel()
        self.data=op()
        self.p=public()
        #self.url=self.data.get_p_url()

    # 不带token不带参的post请求
    def post(self, row, path, data, f2):
        return requests.post(url=self.p.get_n_url(row, path, f2),
                             data=json.dumps(data),
                             headers=self.p.getHeader())

    # 带token不带参的post请求
    def post_t(self, row, t_path, path, data, f2):
        return requests.post(url=self.p.get_n_url(row, path, f2),
                             data=data,
                             headers=self.p.getHeader_token(t_path))

    # 参数可自行输入的post请求(getData001)
    def post_c(self, row, t_path, path,data, f2):
        return requests.post(url=self.p.get_n_url(row, path, f2),
                             data=data,
                             headers=self.p.getHeader_token(t_path))

    # 参数可自行输入的get请求(getData001)
    def get_c(self, row, t_path, path, data, f2):
        return requests.get(url=self.p.get_n_url(row, path, f2),
                            params=json.loads(data),
                            headers=self.p.getHeader_token(t_path))

    # 不带token不带参的get请求
    def get(self, row, path, data, f2):
        return requests.get(url=self.p.get_n_url(row, path, f2),
                            params=json.loads(data),
                            headers=self.p.getHeader())

    # 带token不带参的get请求
    def get_t(self, row, t_path, path,data, f2):
        return requests.get(url=self.p.get_n_url(row, path, f2),
                            params=json.loads(data),
                            headers=self.p.getHeader_token(t_path))

    # url中带两个参数的get请求
    def get_2v(self, row, id1, id2, t_path, path,data, f2):
        return requests.get(url=self.p.get_2v_url(row, id1, id2, path, f2),
                            params=json.loads(data),
                            headers=self.p.getHeader_token(t_path))

    # 带token且url中带参数的get请求
    def get_v(self, row, id, t_path, path, data, f2):
        return requests.get(url=self.p.get_v_url(row, id, path, f2),
                            params=json.loads(data),
                            headers=self.p.getHeader_token(t_path))

    # 带token且url中带参数的post请求
    def post_v(self, row, id, t_path, path, data, f2):
        return requests.post(url=self.p.get_v_url(row, id, path, f2),
                             data=data,
                             headers=self.p.getHeader_token(t_path))

    def post_all(self, row, data, t_path, path, f2):
        return requests.post(url=self.p.get_n_url(row, path, f2),
                             data=json.dumps(data),
                             headers=self.p.getHeader_token(t_path))


