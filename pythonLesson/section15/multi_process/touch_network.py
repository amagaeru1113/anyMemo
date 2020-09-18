import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def worker1(d, lock):
    logging.debug("start")
    with lock:  # withでも記述可能。withの階層が一つならrelease忘れなくて良いかも
        i = d["x"]
        d["x"] = i + 1
        logging.debug(d)
    logging.debug("end")


def worker2(d, lock):
    logging.debug("start")
    with lock:  # withでも記述可能。withの階層が一つならrelease忘れなくて良いかも
        i = d["x"]
        d["x"] = i + 1
        logging.debug(d)
    logging.debug("end")


if __name__ == "__main__":
    d = {"x": 0}
    # lock = threading.Lock()
    # t1 = threading.Thread(target=worker1, args=(d, lock))
    # t2 = threading.Thread(target=worker2, args=(d, lock))

    # 1process 1メモリなのでmain processの中で他のprocessの値は呼び出せない（共有されていない）
    lock = multiprocessing.Lock()
    t1 = multiprocessing.Process(target=worker1, args=(d, lock))
    t2 = multiprocessing.Process(target=worker2, args=(d, lock))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
