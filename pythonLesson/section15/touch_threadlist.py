import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def worker2():
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")


if __name__ == "__main__":
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)  # プログラムが終了した時に同時に終了させる
        t.start()

    print(threading.enumerate())
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()
