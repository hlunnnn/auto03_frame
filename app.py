import os.path

import requests

#封装程序中使用的常量
BASE_URL = "https://twecruitpa.hrtools.cn/"

#获取资源绝对路径
ABS_PATH = os.path.abspath(__file__)
print(ABS_PATH)
#获取文件所属目录
BASE_PATH = os.path.dirname(ABS_PATH)
print(BASE_PATH)

#公共session
session_1 = None