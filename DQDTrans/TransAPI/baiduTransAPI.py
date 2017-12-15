import requests
import hashlib
import random
import urllib

def trans(q,fromLang='en',toLang='zh'):
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    APP_ID = '20171207000102891'
    salt = random.randint(32768,65536)
    SECRETKEY = 'kEiQdms2L6BofZ4uMAmm'
    #sign的生成方法：
    # 将请求参数中的 APPID(appid), 翻译query(q, 注意为UTF-8编码), 随机数(salt),
    # 以及平台分配的密钥(可在管理控制台查看)，按照 appid+q+salt+密钥 的顺序拼接得到字符串1。
    #对字符串1做md5，得到32位小写的sign。
    transstr = APP_ID+q+str(salt)+SECRETKEY
    m = hashlib.md5()
    m.update(transstr.encode('utf-8'))
    sign = m.hexdigest()
    myurl = myurl+'?q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&appid='+APP_ID+'&salt='+str(salt)+'&sign='+sign
    # print(urllib.parse.quote(q))
    print(requests.request('get',myurl).json())
    # print('<--'+q+'-->'+'的翻译结果为：<--'+requests.request('get',myurl).json()['trans_result'][0]['dst']+'-->')
    return requests.request('get',myurl).json()['trans_result'][0]['dst']

# print(trans('Hoy hace buen tiempo.',fromLang='spa',toLang='zh'))