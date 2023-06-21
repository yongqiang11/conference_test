# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : send.py
# Time       ：2023/6/20 15:03
# Author     ：ant
# version    ：python 3.11
# Description：
"""

"""
对requests进行二次封装，封装一个通用的请求方法，返回接口响应的部分数据
通过分析项目接口文档，确认以下信息：
    1.请求方式：get,post
    2.请求体数据：表单形式数据
    3.响应体数据：json格式数据
"""
import requests


class SendMethod:                  # 一个方法中既没有用到cla，或在self,建议申明为静态方法
    @staticmethod
    def request(url, method='get', params=None, data=None):
        """

        :param url: 请求的目标网址
        :param method: 请求的方式 get/post 或者 GET/POST
        :param params: dict
        :param data: dcit
        :return: dict
        """
        # 发送请求
        # 根据method来发起不同的请求
        if method.lower() == 'get':
            response = requests.get(url, params)
        elif method.lower() == 'post':
            response = requests.post(url, data)
        else:
            # 非get/post请求
            response = None

        # 获取响应
        # 如果response不是None
        result = {}
        if response is not None:
            # 获取响应属性
            result['status'] = response.status_code  # 响应状态码
            result['headers'] = response.headers  # 响应头
            result['data'] = response.json()  # 响应体数据
            result['time'] = response.elapsed.microseconds  # 响应时间
        # 如果response是None
        return result


if __name__ == '__main__':
    # 发起请求
    url = 'http://127.0.0.1:8000/api/get_event_list/'
    re = SendMethod.request(url, params={'eid': 1})
    # 获取响应
    print(re)

    

