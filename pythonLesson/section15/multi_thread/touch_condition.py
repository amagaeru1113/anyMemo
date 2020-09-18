import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(condition):
    with condition:
        condition.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


def worker2(condition):
    with condition:
        condition.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")


def worker3(condition):
    with condition:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")
        condition.notifyAll()


if __name__ == "__main__":
    # eventとlockの組み合わせ
    condition = threading.Condition()
    t1 = threading.Thread(target=worker1, args=(condition,))
    t2 = threading.Thread(target=worker2, args=(condition,))
    t3 = threading.Thread(target=worker3, args=(condition,))
    t1.start()
    t2.start()
    t3.start()

# log
# Thread-3: start
# Thread-3: end
# Thread-1: start
# Thread-1: end
# Thread-2: start
# Thread-2: end
