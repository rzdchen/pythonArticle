import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")

# agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhizhu.com",
    "User-Agent": agent,
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive"
}


def is_login():
    # 通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/question/56250357/answer/148534773"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", "wb") as f:
        f.write(response.text.encode("utf-8"))
    print("ok")


def get_captcha():
    # 获取验证码
    import time
    t = str(int(time.time() * 1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login&lang=cn".format(t)
    t = session.get(captcha_url, headers=header)
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)
        f.close()
    from PIL import Image
    try:
        im = Image.open("captcha.jpg")
        im.show()
        im.close()
    except:
        pass
    captcha = input("输入验证码\n")
    return captcha


def get_xsrf():
    # 获取_xsrf
    test_text = '<iden" name="_xsrf" value="1545d4bbfb192d0428ce36ccf74cd6f9"pe="hidden" name="_xsrf" value="1545d4bbfb192d0428ce36ccf74cd6f9"/>'
    response = requests.get("https://www.zhihu.com", headers=header)
    # text_1 = response.text[len(response.text) - 230:len(response.text)].lstrip()
    # match_obj = re.match('.*me(.*?)"', text_1)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text, re.DOTALL)
    if match_obj:
        print(match_obj.group(1))
        return match_obj.group(1)
    else:
        print("没匹配到")
    return ""


def zhihu_login(account, password):
    # 知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "captcha_type": "cn",
            "phone_num": account,
            "password": password
        }
    else:
        if "@" in account:
            # 判断用户名是否为邮箱
            print("邮箱方式登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": "109f18b25debea89e6057cceb3b25933",
                "email": account,
                "captcha_type": "cn",
                "password": password
            }
    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()


# zhihu_login("17091314454", "cc5202012")
# get_index()
# is_login()
# get_xsrf()
get_captcha()
