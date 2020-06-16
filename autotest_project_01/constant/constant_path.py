import os

''' 
# print(__file__)
# print(os.path.dirname(__file__))# 获取文件的 父级路径!
# print(os.path.dirname(os.path.dirname(__file__)))


# 思考一下,我们都需要什么路径?
#     测试用例类路径
#     配置文件路径
#     测试用例数据路径
#     日志文件路径
#     测试报告路径
'''

base_path = os.path.dirname(os.path.dirname(__file__))

#     测试用例类路径:
TestCase_Path = os.path.join(base_path+"/",'cases/')

#     配置文件所在路径
Conf_Path = os.path.join(base_path+"/",'conf/')

#     测试用例数据路径:
Data_Path = os.path.join(base_path+"/",'data/','datas.xlsx')

#     日志文件路径
LogFile_Path = os.path.join(base_path+"/",'log/','log.log')

#     测试报告路径
Report_Path = os.path.join(base_path+"/",'report/','report.html')


#
# print(Data_Path)
# print(Report_Path)
# print(Conf_Path)
