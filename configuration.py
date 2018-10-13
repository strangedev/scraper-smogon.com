import configparser

from lib.frozen_dict import ConfigurationDict


class IniConfiguration(object):

    @staticmethod
    def parseConfigurationFile(file_path: str) -> ConfigurationDict:
        """
        Reads the  test_config.ini file and returns it as a dictionary.
        :param file_path: The relative
        :return:
        """
        config = configparser.ConfigParser()
        config.read(file_path)
        return ConfigurationDict({
            section: ConfigurationDict({
                config_key: config_value
                for config_key, config_value in config[section].items()
            })
            for section in config.sections()
        })


configuration = IniConfiguration.parseConfigurationFile('config.ini')
