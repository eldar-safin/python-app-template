class BaseSettings:
    def dump(self):
        result = {}
        for attr in filter(lambda v: not v.startswith('__'), vars(self.__class__)):
            _value = self.__getattribute__(attr)
            if BaseSettings in _value.__class__.__bases__:
                result[attr] = _value.dump()
            else:
                result[attr] = _value
        return result


class LogSettings(BaseSettings):
    level = 'DEBUG'
    format = '%(asctime)s | %(filename)16s:%(lineno)-4d | %(levelname)-8s | %(message)s'
    time_format = '%Y-%m-%d %H:%M:%S'
    filename = ''
    filemode = 'a'


class Settings(BaseSettings):
    log = LogSettings()


settings = Settings()
