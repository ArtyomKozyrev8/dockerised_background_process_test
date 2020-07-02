import time
import logging


def do_some_work():
    print("Do some work here")
    logging.info("Do some work here")
    time.sleep(1)


def extended_do_work():
    print("Extended do some work here")
    logging.info("Extended do some work here!!!")
    time.sleep(1)
