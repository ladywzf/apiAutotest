#作者:Administrator
#时间:2019/10/19

import sys
sys.path.append(r'C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace')
import json
from apiAutotest.utils import operationExcel
class operationJson:
    def __init__(self):
        self.excel=operationExcel.operationExcel()
    # 获取json文件的内容
    def getReadJson(self, path):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data
    # 以excel表格中data列的值为键，获取在json文件中该键对应的值,f1表示json文件，f2表示excel文件

    def get_json_data(self, row, f1, f2):
        return self.getReadJson(f1)[self.excel.get_data_value(row, f2)]




