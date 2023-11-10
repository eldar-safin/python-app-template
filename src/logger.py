import logging

from settings import settings


class ColoredFormatter(logging.Formatter):
    '''
    Добавляет управляющие символы вокруг записи журнала чтобы она отображалась в цвете
    https://en.wikipedia.org/wiki/ANSI_escape_code#In_shell_scripting
    '''

    ESCAPE_CODES = {
        logging.DEBUG: '\x1b[38;20m',       # серый цвет
        logging.INFO: '\x1b[37;20m',        # белый цвет
        logging.WARNING: '\x1b[33;20m',     # желтый цвет
        logging.ERROR: '\x1b[31;20m',       # красный цвет
        logging.CRITICAL: '\x1b[31;1m'      # красный цвет, жирное начертание
    }

    RESET_CODE = '\x1b[0m'

    def format(self, record):
        record_format = ' '.join([
            self.ESCAPE_CODES.get(record.levelno),
            settings.LOG_FORMAT,
            self.RESET_CODE
        ])
        formatter = logging.Formatter(record_format, settings.LOG_TIME_FORMAT)
        return formatter.format(record)


logger = logging.getLogger()

# Указываем уровень ведения журнала
logger.setLevel(logging.getLevelName(settings.LOG_LEVEL))

# Добавляем журналирование в стандартный вывод
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ColoredFormatter())
logger.addHandler(stream_handler)

# Добавляем журналирование в файл
if settings.LOG_FILENAME:
    file_formatter = logging.Formatter(
        settings.LOG_FORMAT, settings.LOG_TIME_FORMAT)
    file_handler = logging.FileHandler(
        settings.LOG_FILENAME, settings.LOG_FILEMODE)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
