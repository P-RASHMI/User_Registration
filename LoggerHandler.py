import logging

logger = logging

# Basic configuration and required format of the file

logger.basicConfig(filename='C:\\Users\\Charishma\\Desktop\\rashmi\\PYTHONWORK\\User Registration\\userdetails.log',
                    level=logging.INFO, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename='C:\\Users\\Charishma\\Desktop\\rashmi\\PYTHONWORK\\User Registration\\userdetails.log',
                    level=logging.ERROR, format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')