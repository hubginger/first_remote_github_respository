import unittest
import random
from autotest_project_01.site_packages.ddt import ddt, data
from autotest_project_01.common import do_excel, sql_tool, request_tool
from autotest_project_01.common.my_log import my_log
from autotest_project_01.constant.constant_path import Data_Path
from autotest_project_01.common.re_replace import re_replace
from autotest_project_01.common.re_replace import MyData
from autotest_project_01.common.config_read import my_conf


@ddt
class AuditTestCase(unittest.TestCase):
    excel = do_excel.DoExcel(Data_Path, 'audit')
    cases = excel.read_data_object_2()
    # request = request_tool.RequestTool()
    # st = sql_tool.SQLTools()

    @classmethod
    def setUpClass(cls):
        cls.request = request_tool.RequestTool()
        cls.st = sql_tool.SQLTools()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.st.close()
        pass

    def setUp(self):
        # 生成手机号!
        pass

    def tearDown(self):
        # 删除脏数据
        pass



    @data(*cases)
    def test_audit(self, case):
        # 1.我们该sheet页有两种接口
            # 没关系!

        # 2.我们发标之后,我们要拿到这个新发的标的id!
            # 如果是发标,则将id记录下来,记录Excel或者配置文件中!记录到日志都行!(只要记录下来)
            # 如果是审核,我们替换我们的id

        # 数据替换
        case.data = re_replace(case.data)
        case.data = case.data.replace('*id*', self.new_id())

        count_old = 0
        if case.sql_check:
            case.sql_check = re_replace(case.sql_check)
            count_old = self.st.select_count(case.sql_check)

        # 接口调用
        # 创建mock:
        # request = mock.Mock(return_value='{status = 200,message = "注册成功"}')
        response = self.request.request(url=case.url, requestMethod=case.method, json=eval(case.data))

        if case.urlservice == 'publishProgect':
            # 将标id从数据库中查询出来,并记录到MyData类中,(让MyData类有一个属性为:project_id;值为查询出来的值!)
            if str(response.get('status')) == '200':
                sql = 'select id from cola_project where memberId = "'+my_conf.get('data','phoneNumber')+'" and projectType = 0 order by createTime desc limit 1'
                project_id = self.st.select_one(sql)[0]
                setattr(MyData,'project_id',project_id)

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

    def new_id(self):

        return "fdasfdsa"