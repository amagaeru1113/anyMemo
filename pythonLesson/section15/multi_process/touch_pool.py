import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def worker1(i):
    logging.debug("start")
    time.sleep(2)
    logging.debug("end")
    return i


if __name__ == "__main__":
    # t1 = multiprocessing.Process(target=worker1, args=(i,))
    with multiprocessing.Pool(5) as p:  # Pool(N) withの中で動かせるワーカー数
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (100,))
        logging.debug("executed")
        logging.debug(p1.get(timeout=5))
        logging.debug(p2.get(timeout=5))
