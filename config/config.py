class Config(object):
    def __init__(self, args):
        self.load_config_from_dict(args)

    def load_config_from_dict(self, args):
        for key in self.keys:
            value = args.get(key, None)
            if value is not None:
                setattr(self, key, value)

    @property
    def keys(self):
        return list(filter(lambda x: not x.startswith('_'), dir(self)))

    def __getitem__(self, key: str):
        return getattr(self, key)
