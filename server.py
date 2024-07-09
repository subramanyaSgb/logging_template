from logging_config import logger
from main import main_function
import time

def server_function():
    i = 0
    while True:
        logger.error(f'This is a debug message from server{i}.py')
        logger.info('This is an info message from server.py')
        logger.info("_____________________________________________")
        main_function()
        i += 1
        print(i)
        time.sleep(1)
        
if __name__ == '__main__':
    server_function()
