import logging
import os
import sys

import CmdTextColor

logger = logging.getLogger('L')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout)
# handler = logging.FileHandler('C:\\WorkSpace\\temp\\log.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.parent = None


def d(msg):
    if 'PYTHON_LOG_COLOR' in os.environ:
        logger.debug('\033[34m{}\033[0m'.format(msg))
    elif 'PYTHON_LOG_COLOR_CMD' in os.environ:
        CmdTextColor.set_cmd_text_color(CmdTextColor.FOREGROUND_DARKBLUE)
        logger.debug(msg)
        CmdTextColor.resetColor()
    else:
        logger.debug(msg)


def i(msg):
    if 'PYTHON_LOG_COLOR' in os.environ:
        logger.info('\033[32m{}\033[0m'.format(msg))
    elif 'PYTHON_LOG_COLOR_CMD' in os.environ:
        CmdTextColor.set_cmd_text_color(CmdTextColor.FOREGROUND_DARKGREEN)
        logger.debug(msg)
        CmdTextColor.resetColor()
    else:
        logger.info(msg)


def w(msg):
    if 'PYTHON_LOG_COLOR' in os.environ:
        logger.warning('\033[35m{}\033[0m'.format(msg))
    elif 'PYTHON_LOG_COLOR_CMD' in os.environ:
        CmdTextColor.set_cmd_text_color(CmdTextColor.FOREGROUND_DARKPINK)
        logger.debug(msg)
        CmdTextColor.resetColor()
    else:
        logger.warning(msg)


def e(msg):
    if 'PYTHON_LOG_COLOR' in os.environ:
        logger.error('\033[31m{}\033[0m'.format(msg))
    elif 'PYTHON_LOG_COLOR_CMD' in os.environ:
        CmdTextColor.set_cmd_text_color(CmdTextColor.FOREGROUND_RED)
        logger.debug(msg)
        CmdTextColor.resetColor()
    else:
        logger.error(msg)


def c(msg):
    if 'PYTHON_LOG_COLOR' in os.environ:
        logger.critical('\033[33m{}\033[0m'.format(msg))
    elif 'PYTHON_LOG_COLOR_CMD' in os.environ:
        CmdTextColor.set_cmd_text_color(CmdTextColor.FOREGROUND_DARKYELLOW)
        logger.debug(msg)
        CmdTextColor.resetColor()
    else:
        logger.critical(msg)
