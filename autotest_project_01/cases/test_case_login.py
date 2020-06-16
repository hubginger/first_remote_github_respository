import unittest
import random
from autotest_project_01.site_packages.ddt import ddt, data
from autotest_project_01.common import do_excel, sql_tool, request_tool
from autotest_project_01.common.my_log import my_log
from autotest_project_01.constant.constant_path import Data_Path
from autotest_project_01.common.re_replace import re_replace


@ddt
class LoginTestCase(unittest.TestCase):
    excel = do_excel.DoExcel(Data_Path, 'login')
    cases = excel.read_data_object_2()
    request = request_tool.RequestTool()

    @data(*cases)
    def test_login(self, case):
        # 数据替换!
        case.data = re_replace(case.data)
        case.expectation = re_replace(case.expectation)

        #   1.准备数据
        json = eval(case.data)
        expectation = eval(case.expectation)
        description = case.description
        url = case.url
        method = case.method
        row = case.case_id + 1
        #   2.调用接口
        my_log.info('-------->调用' + description + '接口,访问:' + url)
        my_log.info('-------->参数为:' + str(json))

        result = self.request.request(url=url, requestMethod=method, json=json)
        # result = response.json()

        #   3.比对预期和实际结果:
        try:
            self.assertEqual(expectation, result)
        except AssertionError as e:
            print('不通过')
            self.excel.write_result(row, 8, '不通过')
            my_log.info('-------->' + description + '接口测试未通过')
            raise e
        else:
            print('通过')
            my_log.info('-------->' + description + '接口测试通过')
            self.excel.write_result(row, 8, '通过')


@ddt
class RegisterTestCase(unittest.TestCase):
    excel = do_excel.DoExcel(Data_Path, 'register')
    cases = excel.read_data_object_2()
    request = request_tool.RequestTool()
    st = sql_tool.SQLTools()

    @data(*cases)
    def test_register(self, case):

        if '#' in case.data:
            case.data = re_replace(case.data)

        if '*' in case.data:
            phone_number = self.phone_number()
            account_id = self.account_id()
            case.data = case.data.replace('*phoneNumber*',phone_number)
            case.data = case.data.replace('*accountId*',account_id)

        if case.sql_check:
            if '*' in case.sql_check:
                case.sql_check = case.sql_check.replace('*phoneNumber*', phone_number)

        if case.sql_recover:
            if '*' in case.sql_recover:
                case.sql_recover = case.sql_recover.replace('*phoneNumber*', phone_number)

        response = self.request.request(url=case.url, requestMethod=case.method, data=eval(case.data))

        try:
            self.assertEqual(eval(case.expectation), response)

            if case.sql_check:
                result = self.st.select_count(case.sql_check)
                self.assertEqual(1, result)

            if case.sql_recover:
                self.st.delete(case.sql_recover)

        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, 8, '未通过')
            my_log.info('-------->' + case.description + '接口测试未通过')
            print(case.description + '测试未通过')
            my_log.exception(e)
            raise e
        except Exception as e1:
            my_log.exception(e1)

        else:
            self.excel.write_result(case.case_id + 1, 8, '通过')
            my_log.info('-------->' + case.description + '接口测试通过')
            print(case.description + '测试通过')

    def phone_number(self):
        per_list = ['131', '132', '133', '134', '135', '136', '137', '138', '139', '181', '187', '188']
        while True:
            phone = per_list[random.randint(0, len(per_list) - 1)]
            for i in range(8):
                item = str(random.randint(0, 9))
                phone += item
            # 数据库中校验:
            if not sql_tool.SQLTools().select_count('select * from cola_member where phoneNumber = ' + phone):
                return phone


    def account_id(self):
        account = 'kourou_pytest_'
        for i in range(5):
            item = str(random.randint(0, 9))
            account += item
        return account