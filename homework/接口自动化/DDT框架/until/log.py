import logging
import os

from until.untils import Untils

path = os.getcwd()

logger = logging.getLogger('kaoqinglog')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'{Untils.path}\\testcase\\log.log', encoding='utf-8')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(funcName)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
