class LogSettings:
    level = 'DEBUG'
    format = '%(asctime)s | %(filename)16s:%(lineno)-4d | %(levelname)-8s | %(message)s'
    time_format = '%Y-%m-%d %H:%M:%S'
    filename = ''
    filemode = 'a'


class Settings:
    log = LogSettings()


settings = Settings()
