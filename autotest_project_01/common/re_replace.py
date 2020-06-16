import re
from autotest_project_01.common.config_read import my_conf


class MyData():
    # project_id = '40AF6B3F82254D8D87111B7C74882C92'
    # 可以选择,记录到Excel,记录到配置文件,都行!
    # 当然是记录到MyData类中更加方便 ,更加合适!
    pass


def re_replace(data):
    while re.search('#(.+?)#', data):  # 循环退出的条件,是search()方法没有找到#(.+?)#这种形式的字符串!
        replace_data_old = re.search('#(.+?)#', data).group()  # 要替换的双井号:  #phoneNumber#
        key = re.search(r'#(.+?)#', data).group(1)  # 双井号之内的字符串:phoneNumber,作为键去取值

        try:
            replace_data_new = my_conf.get('data', key)  # 从配置文件中取值!
        except:
            replace_data_new = getattr(MyData, 'project_id')

        # data = data.replace(replace_data_old, replace_data_new)
        data = re.sub(replace_data_old, replace_data_new, data)
    return data


if __name__ == '__main__':
    var = '{"phoneNumber":"#phoneNumber#","accountPWD":"#accountPWD#"}'
    print(var)
    print(re_replace(var))

    # 1.分析,我们Excel中,手机号有几个种类:
    # 1.1 手机号未被注册过
    # 1.2 手机号已被注册过
    # 1.3 手机号格式不对(短,长,前缀)

    # 我们要做的事情:
    # 我们想,我们Excel中,已经被注册过的手机号,我们用#phoneNumber#来表示,在代码中进行替换!

    # 1.Excel修改!(*phoneNumber*,#phoneNumber#,#phoneNumber_low#)
    # 2.配置文件;封装re模块;测试用例类:
    # 2.1配置文件:
    #     添加内容即可!

    # 2.2封装re模块:
    # 定义一个方法,完成将Excel中的data,expectation,sql_check,sql_recover列中的对应值替换掉;
    # data, expectation, sql_check中,可能包含*phoneNumber*,#phoneNumber#,#accountPWD#,#accountId#
    # 从配置文件替换!
    # 配置文件中定义了#phoneNumber#,#accountPWD#,#accountId#

    # 2.3修改测试用例类:
    # 判断data,expectation,sql_check,sql_recover列中是否包含#,如果包含#,则调用re_replace()方法,进行替换
    # 替换完重新赋值给case.data,case.expectation.....
