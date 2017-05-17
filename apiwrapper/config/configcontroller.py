import configparser

import os


class ConfigController:
    """A controller class for getting and setting key/value pairs 
    in the config file
    """

    __section_default = 'BunqAPI'
    __dir_path = os.path.dirname(os.path.abspath(__file__))
    __default_filepath = '/%s/parameters.ini' % __dir_path

    def __init__(self, filepath=None):
        """Create an instance of a config controller for getting 
        and setting information
        """

        self.path = self.__default_filepath if filepath is None else filepath
        self.parser = configparser.ConfigParser()
        if self.__section_default not in self.parser.sections():
            self.parser.add_section(self.__section_default)

        self.parser.read(self.path)

    def get(self, name, section=__section_default):
        """Returns a value with a given name from the configuration file."""
        try:
            return self.parser[section][name]
        except KeyError:
            return None

    def set(self, name, val, section=__section_default):
        """Sets an entry in the default section of the config file to a 
        specified value
        :param section: [Optional] The section in which an entry 
        should be changed
        :param name: The entry whose value should be changed
        :param val: The new value for the specified entry
        :return: Nothing, but happiness
        """
        if section not in self.parser.sections():
            self.parser.add_section(section)

        self.parser.set(section, name, val)
        self.save()

    def save(self):
        """Saves the changes to the config file.
        """
        file = open(self.path, 'w')
        self.parser.write(file)
        file.close()
