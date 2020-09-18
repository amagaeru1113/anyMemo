import threading
import multiprocessing

import concurrent.futures
import logging
import time

# concurrent.futures
# 高水準のインターフェース 単純な並列化する場合に使うと良い
# threadで作っておいて、Processはサーバのコア数が増えたら使う

# logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def worker(x, y):
    logging.debug("start")
    r = x * y
    logging.debug(r)
    logging.debug("end")
    return r


def main():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executer:
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executer:
        # f1 = executer.submit(worker, 2, 5)
        # f2 = executer.submit(worker, 2, 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        args = [[2, 2], [5, 5]]
        r = executer.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


if __name__ == "__main__":
    main()
