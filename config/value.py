from .loader import ConfigLoader

PREFIX = 'CONFIG_'


class Value(object):
    def __init__(self, id: str, prefix: str = PREFIX):
        self.id = id
        self.prefix = prefix

    def __call__(self, f):
        result = ConfigLoader.instance(self.prefix).config[self.id]
        return result
