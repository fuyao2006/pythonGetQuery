import pymysql, os, configparser

class ConfigService(object):
    """
    # Config().get_content("user_information")

    配置文件里面的参数
    [notdbMysql]
    host = 192.168.1.101
    port = 3306
    user = root
    password = python123
    """

    def __init__(self, config_filename="myProjectConfig.cnf"):
        file_path = os.path.join(os.path.dirname(__file__), config_filename)
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path)

    def get_sections(self):
        return self.cf.sections()

    def get_options(self, section):
        return self.cf.options(section)

    def get_content(self, section):
        result = {}
        for option in self.get_options(section):
            value = self.cf.get(section, option)
            result[option] = int(value) if value.isdigit() else value
        return result