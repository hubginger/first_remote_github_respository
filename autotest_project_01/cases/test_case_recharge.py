import unittest
import decimal
# from ddt import ddt, data
from autotest_project_01.site_packages.ddt import ddt, data
from autotest_project_01.common import do_excel, sql_tool, request_tool
from autotest_project_01.common.my_log import my_log
from autotest_project_01.constant.constant_path import Data_Path


@ddt
class RechargeTestCase(unittest.TestCase):
    excel = do_excel.DoExcel(Data_Path, 'recharge')
    cases = excel.read_data_object_2()
    request = request_tool.RequestTool()
    st = sql_tool.SQLTools()

    @data(*cases)
    def test_recharge(self, case):

        old_money = 0
        # 先查询!
        if case.sql_check:
            old_money = self.st.select_one(case.sql_check)

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

        result = self.request.request(url=url, requestMethod=method, data=json)
        # result = response.json()

        #   3.比对预期和实际结果:
        try:
            self.assertEqual(expectation, result)

            # 再查询
            if case.sql_check:
                new_money = self.st.select_one(case.sql_check)
                recharge_money_ex = new_money[0] - old_money[0] # Decimal
                recharge_money_re = json.get('holdMoney') # 字符串!
                self.assertEqual(decimal.Decimal(recharge_money_re), recharge_money_ex)

        except AssertionError as e:
            print('不通过')
            self.excel.write_result(row, 8, '不通过')
            my_log.info('-------->' + description + '接口测试未通过')

            raise e
        else:
            print('通过')
            my_log.info('-------->' + description + '接口测试通过')
            self.excel.write_result(row, 8, '通过')


class WithdrawTestCase(unittest.TestCase):
    excel = do_excel.DoExcel(Data_Path, 'withdraw')
    cases = excel.read_data_object_2()
    request = request_tool.RequestTool()
    st = sql_tool.SQLTools()

    @data(*cases)
    def demo_test_recharge(self, case):

        #数据替换!


        old_money = 0
        # 先查询!
        if case.sql_check:
            old_money = self.st.select_one(case.sql_check)

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

        result = self.request.request(url=url, requestMethod=method, data=json)
        # result = response.json()

        #   3.比对预期和实际结果:
        try:
            self.assertEqual(expectation, result)

            # 再查询
            if case.sql_check:
                new_money = self.st.select_one(case.sql_check)

                recharge_money_ex = old_money[0] - new_money[0]  # Decimal

                recharge_money_re = json.get('holdMoney')  # 字符串!
                self.assertEqual(decimal.Decimal(recharge_money_re), recharge_money_ex)

        except AssertionError as e:
            print('不通过')
            self.excel.write_result(row, 8, '不通过')
            my_log.info('-------->' + description + '接口测试未通过')

            raise e
        else:
            print('通过')
            my_log.info('-------->' + description + '接口测试通过')
            self.excel.write_result(row, 8, '通过')
