import re

'''
三个查询
    match()         开头查!开头能匹配到,就返回对象,匹配不到,就返回None
    findall()       一次性将字符串中所有的匹配项查询到,并作为列表返回
    search()        整体查询,匹配字符串中第一次出现的项目,返回一个对象!
    
一个替换
    sub()
    参数:
        替换规则匹配到的字符串!          #phoneNumber#
        替换成什么                       13333333333
        目标字符串                       str1
        数量!                            1/2/3
'''
''' 
# print(re.findall('.','123python456java789'))
# print(re.findall('.','\n\n\n123python456java789'))

# print(re.findall('\d','123python456java789'))
# print(re.findall('\d{3}','123python456java789'))
# print(re.findall('\d{3}','123python456789'))
# print(re.findall('\d{3,6}','123python456789'))
# print(re.findall('\d{3,6}?','123python456789'))
# print(re.findall('\d{3,}','123python456789'))


# print(re.findall('\d*','123python456789'))
# print(re.findall('\d*?','123python456789'))
# print(re.findall('\d+','123python456789'))
# print(re.findall(r'\d+?', '123python456789'))
# print(re.findall(r'\d{1,}?', '123python456789'))


# print(re.findall(r'^hello', '123python456789'))
# print(re.findall(r'^hello', 'hello123python456789'))

# print(re.findall(r'hello$', 'hello123python456789'))
# print(re.findall(r'hello$', 'hello123python456789hello'))



# print(re.findall(r'\bhello', 'hello python,hello java 123'))
# print(re.findall(r'\bhello', 'hello python_hello java 123'))
# print(re.findall(r'hello\b', 'hello python_hello java 123'))
# print(re.findall(r'\bhello\b', 'hello python_hello java 123'))

# print(re.findall(r'\Bhello', 'hello python,hello java 123'))
# print(re.findall(r'hello\B', 'hello python,hello java 123'))
# print(re.findall(r'\Bhello\B', 'hello python,hello java 123'))


# print(re.findall('#(.+?)#','#python#,#java#,#c#,#mysql#,#oracle#,#redis#,#linux#,#html#,#css#,#js#'))
#
# res = re.search('#(.+?)#','#python#,#java#,#c#,#mysql#,#oracle#,#redis#,#linux#,#html#,#css#,#js#')
# print(res)
# print(res.group())
# print(res.group(1))
# # print(res.group(2))


res = re.search('#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#,#(.+?)#','#python#,#java#,#c#,#mysql#,#oracle#,#redis#,#linux#,#html#,#css#,#js#')
print(res.group(1))
print(res.group(2))
print(res.group(3))
print(res.group(4))
print(res.group(5))
print(res.group(6))
print(res.group(7))
print(res.group(8))
print(res.group(9))
print(res.group(10))
# print(res.group(11))
'''

# data_dict = {
#     "phoneNumber": "13333333333",
#     "pwd": "111111",
#     "holdMoney": "10000"
# }

phoneNumber = "13333333333"
pwd = "111111"
holdMoney = "10000"

def re_replace(data):
    # while True:
    #     if re.search('#(.+?)#', data):
    #
    #         replace_data_old = re.search('#(.+?)#', data).group()
    #
    #         key = re.search('#(.+?)#', data).group(1)
    #
    #         replace_data_new = data_dict.get(key)
    #
    #         data = data.replace(replace_data_old, replace_data_new)
    #     else:
    #         return data

    # while True:
    #     if not re.search('#(.+?)#', data):
    #         return data
    #     replace_data_old = re.search('#(.+?)#', data).group()
    #     key = re.search('#(.+?)#', data).group(1)
    #     replace_data_new = data_dict.get(key)
    #     data = data.replace(replace_data_old, replace_data_new)
    while re.search('#(.+?)#', data):
        data = data.replace(re.search('#(.+?)#', data).group(), eval(re.search('#(.+?)#', data).group(1)))
    return data

var = '{"phoneNumber":"#phoneNumber#","pwd":"#pwd#","holdMoney":"#holdMoney#"}'
print(var)
print(re_replace(var))

#
# print(re.search('\d','hello python'))
# print(re.search('#(.+?)#','hello#python#').group())
# print(re.search('#(.+?)#','hello#python#').group(1))



# 注册和登录的测试用例数据中,手机号有哪几类?
    # 1.未被注册的手机号!-------->*phoneNumber*
    # 2.已被注册的手机号!-------->#phoneNumber#
    # 3.前缀,长度不对的手机号!(写一个方法,来生成前缀不对的手机号;配置文件中写入两条数据表示长度太长和太短的手机号!)



