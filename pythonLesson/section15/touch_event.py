import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(event):
    event.wait()
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")


def worker2(event):
    event.wait()
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")


def worker3(event):
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")
    event.set()


if __name__ == "__main__":
    event = threading.Event()
    t1 = threading.Thread(target=worker1, args=(event,))
    t2 = threading.Thread(target=worker2, args=(event,))
    t3 = threading.Thread(target=worker3, args=(event,))
    t1.start()
    t2.start()
    t3.start()

# log
# Thread-3: start
# Thread-3: end
# Thread-1: start
# Thread-2: start
# Thread-1: end
# Thread-2: end
