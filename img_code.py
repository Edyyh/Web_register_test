# -*- coding: utf-8 -*-
import json
import requests

TOKEN = 'de328b742'  # token 获取：http://www.bhshare.cn/imgcode/gettoken
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址


def imgcode_online(img_url):
    """
    在线图片识别
    :param img_url: 在线图片网址 / 图片base64编码（包含头部信息）
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'online',
        'uri': img_url
    }
    response = requests.post(URL, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


def imgcode_local(img_path):
    """
    本地图片识别
    :param img_path: 本地图片路径
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'local'
    }

    # binary上传文件
    files = {'file': open(img_path, 'rb')}

    response = requests.post(URL, files=files, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'

    # 输出样例：
    # {'code': 200, 'msg': 'ok', 'data': '74689'}
    # 74689