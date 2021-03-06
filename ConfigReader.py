import configparser


def read_ini_config(section, key):
    _config = configparser.ConfigParser()
    _config.read('../Config.ini')
    conf = _config.get(section=section, option=key)
    return conf