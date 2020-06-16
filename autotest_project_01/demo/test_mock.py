from unittest import mock
# 开发已经写好代码的基础上!
# 项目比较紧急时候;我们可能会被要求,开发写代码同时,我们写自动化测试代码!

# 我们只要知道有哪些接口,接口有哪些返回!我们就可以写代码了!

url = 'http://www.baidu.com/login'
data = '{user:10086}'
request = mock.Mock(return_value = '{status = 200,message = "注册成功"}')

response = request(url = url,data = data)

# response = request(url=case.url, requestMethod=case.method, json=eval(case.data))

print(response)



