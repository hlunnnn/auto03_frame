#作用：运行并生成html测试报告
#0、导包
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import app
from case.TestLogin import TestLogin
#1、组织测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))

#2、使用htmltestrunner运行测试套件
#2-1、声明测试报告保存文件
file = app.BASE_PATH + "/report/{}.html".format(time.strftime("%Y-%m-%d %H%M%S"))
#2-2、打开文件流执行写操作
with open(file,"wb") as f:
    #2-3、写出运行结果
    runner = HTMLTestRunner(f,title="接口测试报告",description="测试登录业务")
    runner.run(suite)
