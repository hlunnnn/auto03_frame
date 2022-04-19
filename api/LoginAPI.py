import requests
import app

class Login:
    #封装资源路径
    def __init__(self):
        self.login_url = app.BASE_URL + "/wecruit/login/SU6142a94d22d5c64be52a4194"

    #1、登录函数实现
    def login(self,session,username,password,pictureCode):
        myData = {"username": username,
                  "password": password,
                  "pictureCode": pictureCode,
                 }
        response = session.post(self.login_url,data=myData)
        return response




