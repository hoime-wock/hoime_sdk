#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
----------------------------------------
@所属项目 : hoime_sdk
----------------------------------------
@作者     : French<1109527533@hoime.cn>
@软件     : PyCharm
@文件名   : user.py
@创建时间 : 2024/10/3 - 04:03
@修改时间 : 2026/04/09 - 00:38
@文件说明 :
"""
import requests
from typing import Optional, Dict, Any


class UserApi:
    """
    开发人员: French \n
    @创建时间: 2024-05-23 \n
    @修改时间: 2026-04-09 \n
    @功能描述: UserApi对象 \n
    """
    DEFAULT_BASE_URL = "https://user.hoime.vip/api"
    # 设置全局超时时间
    DEFAULT_TIMEOUT = 30
    # 设置版本
    VERSION = "1.0.0.0"

    # 初始化
    def __init__(self, code: str, key: str, base_url: Optional[str] = None, timeout: Optional[int] = None):
        """
        开发⼈员: French \n
        @创建时间: 2024-10-03 \n
        @修改时间: 2026-04-09 \n
        @功能描述: 初始化用户中心 API 客户端 \n

        Args:
            code: 系统 Code
            key: 系统 Key
            base_url: 自定义 API 地址
            timeout: 请求超时时间

        """
        self.code = code
        self.key = key
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.timeout = timeout or self.DEFAULT_TIMEOUT

        self.headers = {
            "HoimeCode": self.code,
            "HoimeKey": self.key,
            "HOIME-SDK-VERSION": self.VERSION
        }

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    # 设置内部方法
    def _post(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        开发人员: French \n
        @创建时间: 2026-04-13 \n
        @修改时间: 2026-04-13 \n
        @功能描述: 统一发送 POST 请求 \n

        Args:
            path: 请求路径
            data: 请求数据

        """
        # 修复：绝对避免双斜杠 // 导致 404
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        return self._request("POST", url, json=data)

    # 设置请求
    def _request(self, method: str, url: str, **kwargs) -> Dict[str, Any]:
        """
        开发人员: French \n
        @创建时间: 2026-04-13 \n
        @修改时间: 2026-04-13 \n
        @功能描述: 统一请求封装，自动处理异常、超时、状态码 \n

        Args:
            method: 请求方式
            url: 请求地址
            kwargs: 请求数据

        """
        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.ConnectionError:
            raise ConnectionError("❌ API 连接失败，请检查网络或服务地址")

        except requests.exceptions.Timeout:
            raise TimeoutError(f"❌ 请求超时（{self.timeout}s）")

        except requests.exceptions.HTTPError as e:
            # 绝对安全获取状态码
            status = response.status_code if 'response' in locals() else '未知'
            raise Exception(f"❌ API 服务异常：状态码 {status} → {str(e)}")

        except ValueError:
            raise Exception("❌ 返回数据不是合法 JSON")

        except Exception as e:
            raise Exception(f"❌ 请求失败：{str(e)}")

    def login(self, email: str, password: str) -> Dict[str, Any]:
        """
        开发人员: French \n
        @创建时间: 2026-04-13 \n
        @修改时间: 2026-04-13 \n
        @功能描述: 用户登录 \n

        Args:
            email: 邮箱
            password: 密码(需要密码原值的MD5, 大写)

        Returns:
            json
        """
        return self._post(
            path="v1/login",
            data={
                "email": email,
                "password": password
            }
        )


if __name__ == '__main__':
    a = UserApi(
        code="123",
        key="123",
    )
    a.login("123", "123")