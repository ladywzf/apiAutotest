#作者:Administrator
#时间:2019/10/19
class excel_data:
    def __init__(self):
        self.caseId=0
        self.url=2
        self.data=3
        self.expect=4
        self.result=5
        self.time=6
    #获取caseId列的列值
    def get_caseId_col(self):
        return self.caseId
    #获取url列的列值
    def get_url_col(self):
        return self.url
    #获取data列的列值
    def get_data_col(self):
        return self.data
    #获取expect列的列值
    def get_expect_col(self):
        return self.expect
    #获取result列的列值
    def get_result_col(self):
        return self.result
    #获取time列的列值
    def get_time_col(self):
        return self.time



