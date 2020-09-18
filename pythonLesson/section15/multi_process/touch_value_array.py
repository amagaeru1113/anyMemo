import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

# Value, Array 違うプロセスの間で共有メモリを扱うのに使う


def f(num, arr):
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)

    for i in range(len(arr)):
        arr[i] *= 2


if __name__ == "__main__":
    num = multiprocessing.Value("f", 0.0)
    arr = multiprocessing.Array("i", [1, 2, 3, 4, 5])

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()
    logging.debug(num.value)
    logging.debug(arr[:])
