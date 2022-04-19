import requests
import app


# 通过登录获取访问权限session
# def get_session(mobile, password):
#     myJson = {}
#     # None 判断
#     if mobile:
#         myJson["mobile"] = mobile
#     if password:
#         myJson["password"] = password
#     session = app.session_1
#     response1 = session.post(app.BASE_URL + "/auth/login/", json=myJson)
#     if response1.status_code == 400:
#         uuid = response1.json().get("error")
#         myParam = {"uuid": uuid}
#         session.get(app.BASE_URL+"/auth/kickOutUserAndLogin", params=myParam)
#     return session
#
# get_session("13771062596","888888")

class Knowledge:
    #封装资源路径
    def __init__(self):
        #查询所有知识目录
        self.get_knwg_dic_url =  app.BASE_URL+"admin-end/directory/getKnwgDirectoryTree/"
        #删除目录
        self.del_dic_url = app.BASE_URL+"/admin-end/directory/delete/"
        #新增目录
        self.add_dic_url = app.BASE_URL+"/admin-end/directory/save/"
        #普通登录
        self.login_url = app.BASE_URL + "/auth/login/"
        #强制登录
        self.login_force_url = app.BASE_URL+"/auth/kickOutUserAndLogin"
        self.get_session("13771062596", "888888")

    def get_session(self,mobile,password):
        myJson = {}
        # None 判断
        if mobile:
            myJson["mobile"] = mobile
        if password:
            myJson["password"] = password
        session =requests.Session()
        response1 = session.post(app.BASE_URL + "/auth/login/", json=myJson)
        if response1.status_code == 400:
            uuid = response1.json().get("error")
            myParam = {"uuid": uuid}
            session.get(app.BASE_URL + "/auth/kickOutUserAndLogin", params=myParam)
        app.session_1 = session

    #1、获取知识目录
    #传参：{}
    #响应体：{"result":{"id":"-1","name":"根目录","directoryChain":"-1","order":0,"updateOrder":-1,"level":1,"knwgNums":42,"isView":true,
    # "children":[{"id":"314362652508725248","parentId":"-1","name":"eeee","directoryChain":"-1/314362652508725248","order":1,"updateOrder":160,"level":1,"knwgNums":24,"isView":true,"corpUserId":""}]},
    #   "state": 200, "success": true, "empty": false}
    def get_knwg_dic(self):
        response = app.session_1.post(self.get_knwg_dic_url,json={})
        return response

    #2、新增知识目录
    #传参：{"name":"44","parentId":"-1"}
    #响应体：{"result": "349235576781398016", "state": 200, "success": true, "empty": false}
    def add_knwg_dic(self,name):
        myjson = {
                    "name":name,
                    "parentId":-1
                  }
        response = app.session_1.post(self.add_dic_url,json=myjson)
        print(response)
        return response

    #3、删除知识目录
    #传参：{"id":"348907475076759552"}
    #响应体：{"result":true,"state":200,"success":true,"empty":false}
    def del_knwg_dic(self,id):
        myjson = {"id":id}
        response = app.session_1.post(self.del_dic_url,json=myjson)
        print(response)
        return response



