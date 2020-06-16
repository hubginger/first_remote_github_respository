import unittest
from MyHTMLTestRunner import HTMLTestRunner
from autotest_project_01.common.my_log import my_log
from autotest_project_01.constant.constant_path import TestCase_Path, Report_Path

#1.加载testsuite;
suite = unittest.TestSuite()


#2.加载测试用例类
loader = unittest.TestLoader()
# suite.addTest(loader.discover(r'D:\Dev\IDE\pycharm\pycharmWorkspace\class01_project_demo\autotest_project_01\cases'))
suite.addTest(loader.discover(TestCase_Path))


#3.运行!
my_log.info('---->执行测试开始!')
# with open(r'D:\Dev\IDE\pycharm\pycharmWorkspace\class01_project_demo\autotest_project_01\report\report.html','wb') as fwb:
with open(Report_Path,'wb') as fwb:
    runner = HTMLTestRunner(stream=fwb, verbosity=2,title="测试接口",description='第一次测试接口',tester='扣肉')
    runner.run(suite)
my_log.info('---->执行测试结束!')

# 邮件发送的代码:
