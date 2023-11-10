#!/usr/bin/env python3

import sys

from logger import logger
from helpers import clear_console


def main():
    clear_console()
    logger.debug('main')


if __name__ == '__main__':
    sys.exit(main())
