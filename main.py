from background_process.libs import some_library
import logging
from logging.handlers import TimedRotatingFileHandler
import time
from datetime import datetime


logging.basicConfig(
    handlers=[TimedRotatingFileHandler("logs/logfile.txt", when="midnight", interval=1)],
    format='%(levelname)s - %(asctime)s - %(message)s - ModuleName: %(module)s',
    level=logging.INFO
)

if __name__ == '__main__':
    while True:
        some_library.do_some_work()
        some_library.extended_do_work()
        logging.warning("New Changes")
        logging.info("small new changes")
        print(f"ABC {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        with open("logs/app.txt", mode='a') as f:
            f.write("new changes\n")
        time.sleep(1)
