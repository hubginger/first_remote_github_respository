import logging
from autotest_project_01.common.config_read import my_conf
from autotest_project_01.constant.constant_path import LogFile_Path


log_level = my_conf.get('logs','log_level')
console_level = my_conf.get('logs','console_level')
file_level = my_conf.get('logs','file_level')
file_name = my_conf.get('logs','file_name')
# path = r'D:\Dev\IDE\pycharm\pycharmWorkspace\class01_project_demo\autotest_project_01\log'
# file_path = os.path.join(LogFile_Path,file_name)

class MyLogger():
    def __new__(cls, *args, **kwargs):

        my_logger = logging.getLogger('my_logger')
        my_logger.setLevel(log_level)

        sh = logging.StreamHandler()
        sh.setLevel(console_level)

        my_logger.addHandler(sh)

        file_log = logging.FileHandler(LogFile_Path, 'a', encoding='UTF-8')
        file_log.setLevel(file_level)
        my_logger.addHandler(file_log)

        format = '%(asctime)s -- Thread [%(threadName)s:%(thread)d] -- code [%(filename)s :line:%(lineno)d] -- %(levelname)s ---- %(message)s'
        sh.setFormatter(logging.Formatter(format))
        file_log.setFormatter(logging.Formatter(format))

        return my_logger

my_log = MyLogger()

