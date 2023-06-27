# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : event_case.py
# Time       ：2023/6/26 15:22
# Author     ：ant
# version    ：python 3.11
# Description：
"""
import unittest
from interface.event_api import EventApi
"""
该模块存放发布会测试用例
一个方法编写一个测试用例
"""


class EventCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.event_api = EventApi('http://127.0.0.1:8000')

    def test_add_event(self):
        """
        测试添加发布会接口
        :return:
        """
        payload = {
            'eid': '300',
            'name': '荣耀300发布会',
            'limit': 20,
            'status': 1,
            'address': '成都',
            'start_time': '2023-10-10 11:10:11'
        }
        # 请求发布会接口,获取响应
        result = self.event_api.add_event(payload)
        # 提取实际结果和预期结果进行断言
        # data.status = 10200
        # 如果result是一个空字典，就直接将result设置为None
        if result:
            status = result.get('data', {}).get('status', {})
        else:
            status = None
        self.assertEqual(status, 10200)
        print(status)

    # def query_event(self):
    #     # 请求查询发布会接口
    #     result = self.event_api.query_event(300)
    #     # 提取实际结果和预期结果进行断言



if __name__ == '__main__':
    unittest.main(verbosity=2)

