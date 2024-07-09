from logging_config import logger

def main_function():
    logger.error('This is a debug message from main.py')
    logger.info('This is an info message from main.py')

if __name__ == '__main__':
    main_function()

