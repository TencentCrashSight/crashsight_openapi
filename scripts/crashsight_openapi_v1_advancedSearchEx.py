# coding: utf-8
import requests
import time
import base64
import hmac
import hashlib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class crashsightOpenApi(object):
    def __init__(self, localUserId, userOpenapiKey, request_url, body):
        self.localUserId = localUserId
        self.headers = {
            'Content-Type': 'application/json',
            'Accept-Encoding': '*'
        }
        self.userOpenapiKey = userOpenapiKey
        self.request_url = request_url
        self.body = body
        self.localUserId = localUserId

        # 获取当前时间戳
        self.t = int(time.time())

    """
        获取签名计算值的方法
    """

    def __get_api_signature(self):
        key_bytes = bytes(self.userOpenapiKey, 'utf-8')
        message = self.localUserId + '_' + str(self.t)
        message_bytes = bytes(message, 'utf-8')
        hash_str = hmac.new(key_bytes, message_bytes, digestmod=hashlib.sha256).hexdigest()
        # print(hash_str)

        hash_str_64 = base64.b64encode(bytes(hash_str, encoding="utf8"))
        hash_str_64 = str(hash_str_64, encoding="utf-8")
        # print(hash_str_64)

        return hash_str_64

    """
        获取相关的接口返回数据
    """

    def do_post_request(self):
        # print(self.request_url)
        self.request_url += (
            '?userSecret={}&localUserId={}&t={}'.format(self.__get_api_signature(), self.localUserId, str(self.t)))
        print(self.request_url)
        api_response = requests.post(self.request_url, data=json.dumps(self.body), headers=self.headers)
        return api_response


if __name__ == "__main__":

    localUserId = 'xxx'
    userOpenapiKey = 'xxx'
    app_id = '3729de3c06'
    request_url = 'https://crashsight.qq.com/uniform/openapi/advancedSearchEx'

    body = {"start": "0", "sortField": "imeiCount", "desc": True, "pid": "1",
            "searchConditionGroup": {"conditions": [{"field": "version"}, {"field": "exceptionType"}]},
            "appId": "3729de3c06", "platformId": 1, "rows": 10}
    # print(request_url)

    crashsight_open_api_obj = crashsightOpenApi(localUserId, userOpenapiKey, request_url, body)
    result = crashsight_open_api_obj.do_post_request()
    print(result.content)