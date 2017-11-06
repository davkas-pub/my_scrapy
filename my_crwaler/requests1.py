import requests
import time
import my_crwaler.utils.common as utils


def sqParams():
    domain = 'http://101.132.69.89:8071/app_dev.php/api/fish/simplified/sq/login'
    now = int(time.time())
    params = {
        "user_name": "pw1234",
        "server_id": "1",
        "is_adult": "1",
        "pt_vip": "1",
        "time": now
    }

    string = ""
    for v in params:
        string += str(params.get(v))
    key = 'yFTq1x^SdVjxBr&@^68mZ^0dcA8YwjpR'
    key = '123456789'
    string += key
    print(string)
    sign = utils.get_md5(string)
    params['sign'] = sign

    return domain, params

def sqCheckParams():
    domain = 'http://101.132.69.89:8071/app_dev.php/api/fish/simplified/sq/checkUser'
    now = int(time.time())
    params = {
        "server_id": "1",
        "user_name": "pw1234",
        "time": now
    }

    string = ""
    for v in params:
        string += str(params.get(v))
    key = 'yFTq1x^SdVjxBr&@^68mZ^0dcA8YwjpR'
    key = '123456789'
    string += key
    print(string)
    sign = utils.get_md5(string)
    params['sign'] = sign

    return domain, params


def setParams():
    domain = 'http://101.132.69.89:8071/app.php/api/fish/simplified/union/login'
    now = int(time.time())
    params = {
        'site': "douyu",
        "user_name": "pw123",
        "is_adult": "1",
        "client": "1",
        "time": now,
        "server_id": "1"
    }

    sort_keys = sorted(params.keys())
    string = ""
    for i in range(len(sort_keys)):
        string += str(params[sort_keys[i]])
    key = 'yFTq1x^SdVjxBr&@^68mZ^0dcA8YwjpR'
    key = '123456789'
    string += key
    print(string)
    sign = utils.get_md5(string)
    params['sign'] = sign

    return domain, params


def payParams():
    domain = 'http://101.132.69.89:8071/app_dev.php/api/fish/simplified/union/pay'
    now = int(time.time())
    params = {
        'orderno': "pw"+str(now),
        "user_name": "pw123",
        "point": "1000",
        "payway": "1",
        "money": 100,
        "moneytype": "CNY",
        "time": now,
        "server_id": "1",
        "site": "douyu"
    }

    sort_keys = sorted(params.keys())
    string = ""
    for i in range(len(sort_keys)):
        string += str(params[sort_keys[i]])
    key = 'yFTq1x^SdVjxBr&@^68mZ^0dcA8YwjpR'
    key = '987654321'
    string += key
    print(string)
    sign = utils.get_md5(string)
    params['sign'] = sign

    return domain, params


def paySqParams():
    domain = 'http://101.132.69.89:8071/app_dev.php/api/fish/simplified/sq/pay'
    now = int(time.time())
    params = {
        'order_id': ("DY"+str(now)),
        "user_name": "pw1234",
        "server_id": "1",
        "coin": "1000",
        "money": 100,
        "time": now,
    }

    string = ""
    for v in params:
        string += str(params.get(v))

    key = '987654321'
    string += key
    print(string)
    sign = utils.get_md5(string)
    params['sign'] = sign

    return domain, params

def checkUserParams():
    domain = 'http://101.132.69.89:8071/app_dev.php/api/fish/simplified/union/checkUser'
    now = int(time.time())
    params = {
        'site': "douyu",
        "user_name": "pw123",
        "time": now,
        "server_id": "1"
    }

    sort_keys = sorted(params.keys())
    string = ""
    for i in range(len(sort_keys)):
        string += str(params[sort_keys[i]])
    key = 'yFTq1x^SdVjxBr&@^68mZ^0dcA8YwjpR'
    key = '123456789'
    string += key
    print(string)
    sign = utils.get_md5(string)
    params['sign'] = sign

    return domain, params

def request(domain, params):
    response = requests.get(url=domain, params=params)
    print(response.url)


def main():
    domain, params = checkUserParams()
    request(domain, params)


if __name__ == '__main__':
    main()
