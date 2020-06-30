from background_process.libs import some_library
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

if __name__ == '__main__':
    while True:
        some_library.do_some_work()
