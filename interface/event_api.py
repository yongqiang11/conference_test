# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : event_api.py
# Time       ：2023/6/21 10:39
# Author     ：ant
# version    ：python 3.11
# Description：
"""
# 定义发布会模块的接口
# 这个接口类针对的是一个业务模块：发布会模块
from common.send import SendMethod


class EventApi:
    def __init__(self, host):
        self.host = host

    def add_event(self, payload, method='post'):
        """
        添加发布会
        :param method: 添加发布会的请求方法
        :param payload: 添加发布会的请求数据
        :return: 响应结果
        """
        url = self.host + '/api/add_event/'
        result = SendMethod.request(url, data=payload)
        return result

    def query_event(self, method='get', eid=None, name=None):
        """
        查询发布会的接口
        :param method:查询发布会的请求方法
        :param eid:发布会id
        :param name: 发布会标题
        :return:响应结果
        """
        if eid:
            params = {'eid': eid}
        elif name:
            params = {'name': name}
        else:
            return {}
        url = self.host + '/api/get_event_list/'
        result = SendMethod.request(url, method='get', params=params)
        return result


if __name__ == '__main__':
    event_api = EventApi('http://127.0.0.1:8000')
    """
  
    # 调用添加发布会
    data = {
        'eid': '298',
        'name': '荣耀20发布会',
        'limit': 20,
        'status': 1,
        'address': '成都',
        'start_time': '2023-10-10 11:10:11'
    }
    result1 = event_api.add_event(payload=data)
    print(result1)
      """

    # 调用查询发布会
    # result2 = event_api.query_event(eid=298)
    result2 = event_api.query_event(name='荣耀20发布会')
    print(result2)
