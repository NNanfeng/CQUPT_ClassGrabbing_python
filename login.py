import requests
import base64

#获取验证码，使用百度orc
def get_code(img):
    token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=0cOn0xG4CqNcqhZYgx7gVLuY&client_secret=uGG6vL5ZHTWXYt6yHKmjXA23SP9MIYdh'
    response = requests.get(token_url)
    if response:
        access_token=response.json()["access_token"]
    orc_url="https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"

    params = {"image":img}
    request_url = orc_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        code=response.json()["words_result"][0]["words"]
    return code


def login(id,psw):
    header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
    }

    host_url="http://xk1.cqupt.edu.cn/"
    checkcode="createValidationCode.php"
    login="checkLogin.php"

    sesssion=requests.session()#创建一个用户会话
    while(True):#循环尝试登陆
        res=sesssion.get(url=host_url+checkcode,headers=header)#为这个会话获取验证码并设定cookie
        img=base64.b64encode(res.content)

        payload={
            "id":id,
            "psw":psw,
            "vCode":get_code(img)#通过百度orc获取
        }

        res=sesssion.post(host_url+login,data=payload,headers=header)
        if not res.json()["code"]:
            return sesssion

