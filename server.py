from logging_config import logger
from main import main_function
import time
import threading
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
        
def test_1():
    for i in range(100):
        logger.info(f'Test_1 Functino called - {i}')
    
if __name__ == '__main__':
    ServerTestThread = threading.Thread(target=test_1)
    ServerTestThread.start()
    server_function()
