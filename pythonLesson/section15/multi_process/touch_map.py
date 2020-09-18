import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def worker1(i):
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")
    return i


if __name__ == "__main__":
    with multiprocessing.Pool(5) as p:  # mapで複数のワーカーを記述できる
        # r = p.map(worker1, [100, 200])  # リストで渡した値に関するプロセスが全て終了したら以下のloggingが通る
        # r = p.map_async(worker1, [100, 200])  # asyncにすると次の処理に写して、processは後ろで動かせる -> r.get()する
        r = p.imap(worker1, [100, 200])  # asyncにすると次の処理に写して、processは後ろで動かせる
        logging.debug("executed")

        # logging.debug(r)
        # logging.debug(r.get())
        logging.debug([i for i in r])

        # p1 = p.apply_async(worker1, (100,))
        # p2 = p.apply_async(worker1, (100,))
        # logging.debug("executed")
        # logging.debug(p1.get())
        # logging.debug(p2.get())
