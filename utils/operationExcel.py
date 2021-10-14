#作者:Administrator
#时间:2019/10/19
import xlrd
from utils.public import *
from utils.excel_data import excel_data
class operationExcel:
    # 初始化
    def __init__(self):
        self.exdata = excel_data()

    # 获取excel表格
    def getExcel(self, path):
        db = xlrd.open_workbook(path)
        sheet = db.sheet_by_index(0)
        return sheet

    # 获取单元格的值
    def get_cell_value(self, row, col, path):
        return self.getExcel(path).cell_value(row, col)

    # 获取caseId的值
    def get_caseId_value(self, row, path):
        return self.get_cell_value(row, self.exdata.get_caseId_col(), path)

    # 获取url的值
    def get_url_value(self, row, path):
        return self.get_cell_value(row, self.exdata.get_url_col(), path)

    # 获取data列的值
    def get_data_value(self, row, path):
        return self.get_cell_value(row, self.exdata.get_data_col(), path)





