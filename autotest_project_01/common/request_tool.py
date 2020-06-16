import requests


# 封装请求!
class RequestTool():

    def request(self,url,requestMethod,headers = None,data = None,json = None):
        rm = requestMethod.lower()
        if rm == 'get':
            response = requests.get(url = url,headers = headers,params = data)
        elif rm == 'post':
            response = requests.post(url = url,headers = headers,json = json)
        return response.json()


class SessionTools():

    def __init__(self):
        self.session = requests.session()

    def session_request(self,url,requestMethod,headers = None,data = None,json = None):
        rm = requestMethod.lower()
        if rm == 'get':
            response = self.session.get(url=url, headers=headers, params=data)
        elif rm == 'post':
            response = self.session.post(url=url, headers=headers, data=data, json=json)
        return response.content.decode('utf-8')

    def close(self):
        self.session.close()




# 当我们想要封装某功能时候;
# 我们先想想,封装之后的调用方式是怎样的(封装的效果是啥!)
# 然后我们通过这个效果,来思考,我们的封装怎么写!