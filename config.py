import ConfigParser

def readCfg(cfg_file):
    config = ConfigParser.ConfigParser()
    config.read(cfg_file)

    return config
