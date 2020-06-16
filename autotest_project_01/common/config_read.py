from configparser import ConfigParser
from autotest_project_01.constant.constant_path import Conf_Path
import os
#
class MyConf(ConfigParser):

    def __init__(self):
        # 先读取switch_env配置文件!
        # 根据env的值,去判断再读取哪个配置文件!
        cp = ConfigParser()
        cp.read(os.path.join(Conf_Path+'/','switch_env.ini'),encoding='utf8')

        env = cp.getint('switch','env')

        super(MyConf, self).__init__()

        if env ==  1:
            self.read(os.path.join(Conf_Path+'/','conf_1.ini'), encoding='UTF-8')
            pass
        elif env == 2:
            self.read(os.path.join(Conf_Path+'/','conf_2.ini'), encoding='UTF-8')
            pass
        elif env == 3:
            self.read(os.path.join(Conf_Path+'/','conf_3.ini'), encoding='UTF-8')
            pass
        else:
            self.read(os.path.join(Conf_Path+'/','conf_1.ini'), encoding='UTF-8')
            pass

my_conf = MyConf()


# print(Conf_Path)
#
# print(
#     my_conf.get('logs','log_level')
# )