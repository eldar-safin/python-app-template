import logging

from settings import settings


class ColoredFormatter(logging.Formatter):
    '''
    Добавляет управляющие символы вокруг записи журнала чтобы она отображалась в цвете
    https://en.wikipedia.org/wiki/ANSI_escape_code#In_shell_scripting
    '''

    ESCAPE_CODES = {
        logging.DEBUG: '\x1b[37;20m',       # серый цвет
        logging.INFO: '\x1b[38;20m',        # белый цвет
        logging.WARNING: '\x1b[33;20m',     # желтый цвет
        logging.ERROR: '\x1b[31;20m',       # красный цвет
        logging.CRITICAL: '\x1b[31;1m'      # красный цвет, жирное начертание
    }

    RESET_CODE = '\x1b[0m'

    def format(self, record):
        record_format = ' '.join([
            self.ESCAPE_CODES.get(record.levelno),
            settings.log.format,
            self.RESET_CODE
        ])
        formatter = logging.Formatter(record_format, settings.log.time_format)
        return formatter.format(record)


logger = logging.getLogger()

# Указываем уровень ведения журнала
logger.setLevel(logging.getLevelName(settings.log.level))

# Добавляем журналирование в стандартный вывод
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ColoredFormatter())
logger.addHandler(stream_handler)

# Добавляем журналирование в файл
if settings.log.filename:
    file_formatter = logging.Formatter(
        settings.log.format, settings.log.time_format)
    file_handler = logging.FileHandler(
        settings.log.filename, settings.log.filemode)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
