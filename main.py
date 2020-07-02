from background_process.libs import some_library
import logging
import time

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, filename="logs/logfile.txt")

if __name__ == '__main__':
    while True:
        some_library.do_some_work()
        some_library.extended_do_work()
        with open("logs/app.txt", mode='a') as f:
            f.write("xyz\n")
        time.sleep(1)
