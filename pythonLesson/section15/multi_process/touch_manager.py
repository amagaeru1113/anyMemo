import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

# Manager サーバープロセスを管理
# プロセスの間でデータをやり取りする
# ValueやArrayよりは遅い


def worker1():
    l.reverse()
    d["x"] += 1
    n.y += 1


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        l = manager.list()
        d = manager.dict()
        n = manager.Namespace()

        l.append(1)
        l.append(2)
        l.append(3)
        d["x"] = 20
        n.y = 0

        p1 = multiprocessing.Process(target=worker1, args=(l, d, n))
        p1.start()
        p1.join()

        logging.debug(l)
        logging.debug(d)
        logging.debug(n)

