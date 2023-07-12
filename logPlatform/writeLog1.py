# coding:utf-8



import logging

import logging.handlers

import random

import time



logger = logging.getLogger(__name__)



logger = logging.getLogger('mypython_logger')

# Log等级总开关

logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件

logfile = 'my_python.log'

# 输出到控制台

# ch = logging.StreamHandler()

# ch.setLevel(logging.DEBUG)

# 按天数轮转，保存5份

trh = logging.handlers.TimedRotatingFileHandler(logfile, when='h', interval=1, backupCount=32, encoding='utf-8')

trh.setLevel(logging.DEBUG)

# 按大小删除

#rh = logging.handlers.RotatingFileHandler(logfile, maxBytes=512 * 1024 * 1024, backupCount=5, encoding='utf-8')

#rh.setLevel(logging.DEBUG)

# 定义handler的输出格式

formatter = logging.Formatter("%(asctime)s - %(pathname)s - %(process)d - %(levelname)s: %(message)s")

# ch.setFormatter(formatter)

trh.setFormatter(formatter)

#rh.setFormatter(formatter)

# 将logger添加到handler里面

# logger.addHandler(ch)

#logger.addHandler(rh)

logger.addHandler(trh)



Name_list = ['我还是从前那个少年', '我还是从前那个少年', '种在心中信念丝毫未减', '眼前这个少年', '还是最初那张脸']



while True:

    _locat_name = random.choice(Name_list)

    logger.info(_locat_name)

    logger.debug(_locat_name)

    logger.warning(_locat_name)

    logger.info(_locat_name)

    time.sleep(0.00005)
