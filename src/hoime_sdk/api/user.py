# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
----------------------------------------
@所属项目 : hoime_sdk
----------------------------------------
@作者     : French<1109527533@hoime.cn>
@软件     : PyCharm
@文件名   : user.py
@创建时间 : 2024/10/3 - 04:03
@修改时间 : 2024/10/3 - 04:03
@文件说明 :
"""
import requests


class UserApi(object):
    """
    开发人员: French \n
    @创建时间: 2022-05-23 \n
    @修改时间: 2022-05-23 \n
    @功能描述: UserApi对象 \n
    """
    def __init__(self, code, key, base_url=None):
        """
        开发人员: French \n
        @创建时间: 2024-10-03 \n
        @修改时间: 2024-10-03 \n
        @功能描述: 初始化 \n

        Args:
            code(str): 系统Code
            key(str): 系统Key
            base_url(str): API基础地址

        Returns:
            float
        """
        self.code = code
        self.key = key
        self.base_url = "http://user.hoime.vip/api"
        # 设置请求头
        self.headers = {
            "Code": self.code,
            "Key": self.key
        }
        # 是否赋值BaseUrl
        if base_url is not None:
            self.base_url = base_url

    def login(self, email, password):
        """
        开发人员: French \n
        @创建时间: 2024-10-03 \n
        @修改时间: 2024-10-03 \n
        @功能描述: 用户登录 \n

        Args:
            email(str): 邮箱
            password(str): 密码(需要密码原值的MD5, 大写)

        Returns:
            json
        """
        url = self.base_url + "/login"
        data = {
            "email": email,
            "password": password
        }
        try:
            response = requests.post(url=url, headers=self.headers, json=data)
            return response.json()
        except requests.exceptions.ConnectionError:
            print("请求失败")
