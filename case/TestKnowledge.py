import time
import unittest

from api.KnowledgeAPI import Knowledge


class TestKnowledge(unittest.TestCase):
    #初始化函数，创建Login对象
    knwg_id = None

    @classmethod
    def setUpClass(cls):
        cls.knwg = Knowledge()
        TestKnowledge.knwg_id = ""


    @classmethod
    def tearDownClass(cls):
        # self.session.close()
        pass
    # 测试函数1：查询知识目录
    def test1_get_knwg_dic(self):
        response = self.knwg.get_knwg_dic()
        self.assertEqual(200,response.status_code)
        self.assertIn("根目录",response.text)


    #测试函数2：新增知识目录
    def test2_add_knwg_dic(self):
        response = self.knwg.add_knwg_dic("测试目录10")
        print("新增知识返回信息：",response.text)
        TestKnowledge.knwg_id = response.json().get("result")
        self.assertEqual(200,response.status_code)

    #测试函数3：删除知识目录
    def test3_del_knwg_dic(self):
        response = self.knwg.del_knwg_dic(TestKnowledge.knwg_id)
        print("删除知识返回信息：",response.text)
        self.assertEqual(200, response.status_code)

