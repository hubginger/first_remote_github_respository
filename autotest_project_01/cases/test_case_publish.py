import unittest
import random
from autotest_project_01.site_packages.ddt import ddt, data
from autotest_project_01.common import do_excel, sql_tool, request_tool
from autotest_project_01.common.my_log import my_log
from autotest_project_01.constant.constant_path import Data_Path
from autotest_project_01.common.re_replace import re_replace


@ddt
class PublishTestCase(unittest.TestCase):
    excel = do_excel.DoExcel(Data_Path, 'publish')
    cases = excel.read_data_object_2()
    request = request_tool.RequestTool()
    st = sql_tool.SQLTools()

    @data(*cases)
    def test_publish(self, case):

        '''
        1.准备数据
        2.调用接口
        3.比对结果


        1.数据替换,执行sql
        2.调用接口,执行sql
        3.不对结果,比对sql
        '''

        # 数据替换
        case.data = re_replace(case.data)
        phone_number = self.phone_number()
        case.data = case.data.replace('*phoneNumber*', phone_number)
        count_old = 0
        if case.sql_check:
            case.sql_check = re_replace(case.sql_check)
            count_old = self.st.select_count(case.sql_check)

        # 接口调用
        response = self.request.request(url=case.url, requestMethod=case.method, json=eval(case.data))

        # 返回断言
        try:
            self.assertEqual(eval(case.expectation), response)

            if case.sql_check:
                count_new = self.st.select_count(case.sql_check)
                self.assertEqual(count_new, count_old + 1)

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
