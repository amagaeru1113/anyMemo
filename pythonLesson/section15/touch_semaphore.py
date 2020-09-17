import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(semaphore):
    with semaphore:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def worker2(semaphore):
    with semaphore:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def worker3(semaphore):
    with semaphore:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


if __name__ == "__main__":
    # semaphore は実行するスレッド数を制御可能
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(semaphore,))
    t2 = threading.Thread(target=worker2, args=(semaphore,))
    t3 = threading.Thread(target=worker3, args=(semaphore,))
    t1.start()
    t2.start()
    t3.start()

# log
# root@sample-db:/code/section15# python touch_semaphore.py
# Thread-1: start
# Thread-2: start
# Thread-1: end
# Thread-2: end
# Thread-3: start
# Thread-3: end
