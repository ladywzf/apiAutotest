import sys
sys.path.append(r'C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace')
import HTMLTestReport
from apiAutotest.tests.test_be import *
import time
if __name__ == '__main__':
    test_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"tests")
    testcase=unittest.defaultTestLoader.discover(r'C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\apiAutotest\tests',pattern='test*.py')
    #testcase = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    #now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    filepath = r"E:\\{0}".format(os.path.basename(os.path.dirname(os.path.dirname(__file__))))+r"\\reports\\{0}\\".format(fileName)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    ls = os.listdir(filepath)
    for i in ls:
        c_path = os.path.join(filepath, i)
        os.remove(c_path)
    path = filepath + "{0}.html".format(fileName)
    fp = open(path, mode="wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title="自动化测试报告", description="apiAutotest")
    runner.run(testcase)
    fp.close()
