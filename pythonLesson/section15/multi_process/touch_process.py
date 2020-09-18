from multiprocessing import (
    Process,
    Lock,
    RLock,
    Semaphore,
    Queue,
    Event,
    Condition,
    Barrier,
    Value,
    Array,
    Pipe,
    Manager,
)

import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def worker1(i):
    logging.debug("start")
    logging.debug(i)
    time.sleep(2)
    logging.debug("end")


def worker2(i):
    logging.debug("start")
    logging.debug(i)
    logging.debug("end")


if __name__ == "__main__":  # 他のコードで呼び出されるとマルチプロセスが動く
    i = 2
    t1 = multiprocessing.Process(target=worker1, args=(i,))
    t2 = multiprocessing.Process(name="renamed worker2", target=worker2, args=(i,))
    t1.start()
    t2.start()
