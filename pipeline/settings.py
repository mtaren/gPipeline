import os

import utils.singleton as singleton

"""
todo: implement lock functionality, maybe a decorator to check for a lock
    before assigning a new setting.



Settings path is 
"""


def sanitize_str(s):
    """
    Called when reading in the settings file on each string
    1. used to convert strings to booleans when needed
    2. can also check if it is a valid string, special chars, etc.
    :param s: 
    :return: 
    """
    if s.lower() == 'true':
        return True
    if s.lower() == 'false':
        return False
    return s


class PipelineSettings(metaclass=singleton.Singleton):
    def __init__(self):
        self.clean = True  # rerun everything, ignore cached results
        self.default_executor = 'local'
        self.default_result_store = 'local'

    def init_default_settings(self):
        # get current working dir, then find the default settings file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        conf = os.path.join(current_dir, os.pardir, 'default.conf')

        # parse default file
        with open(conf, 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                if line.startswith('#'):
                    continue
                linespl = line.split('=')
                setting = linespl[0]
                value = linespl[1]

                if hasattr(self, setting):
                    setattr(self, setting, sanitize_str(value))
                else:
                    raise Exception("Error, no such setting: " + setting)


