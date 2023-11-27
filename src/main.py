#!/usr/bin/env python3

import sys

from settings import settings
from logger import logger
from helpers import clear_console


def main():
    clear_console()
    logger.debug(f'Settings:\n{settings.dump()}')


if __name__ == '__main__':
    sys.exit(main())
