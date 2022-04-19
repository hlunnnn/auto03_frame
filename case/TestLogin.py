import json
import unittest

import requests
from parameterized import parameterized
import app
from api.LoginAPI import Login

#读取json文件
def read_from_json():
    #1.创建空列表接收数据
    data = []
    #2、创建文件流，使用json解析，并将解析的结果转换为元组添加到列表
    with open(app.BASE_PATH+"/data/login_case.json","r",encoding="utf-8") as f:
        all = json.load(f).values()
        print(all)
        print(type(all))
        for item in all:
            username = item.get("username")
            password = item.get("password")
            pictureCode = item.get("pictureCode")
            state = item.get("state")
            case_one = (username,password,pictureCode,state)
            data.append(case_one)
    #3、返回列表
    print(data)
    return data



class TestLogin(unittest.TestCase):

    #初始化函数，创建Login对象
    def setUp(self):
        self.session = requests.Session()
        self.login  = Login()

    def tearDown(self):
        self.session.close()

    #测试函数1：测试登录
    #测试数据动态导入
    #1.parameterized注解导入参数
    #2.将数据封装进文件
    #3.从外部文件读取数据并组织列表，然后导入parameterized.expand
    @parameterized.expand(read_from_json)
    def test_login(self,mobile,password,pictureCode,state):
        response = self.login.login(self.session,mobile,password,pictureCode)
        print(response.json())
        #断言判断
        self.assertEqual(state,response.json().get("state"))

