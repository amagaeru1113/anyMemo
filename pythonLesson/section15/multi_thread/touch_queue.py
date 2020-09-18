import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(queue):
    logging.debug("start")
    # queue.put(100)  # [100, 200] first in first out
    # time.sleep(3)
    # queue.put(200)

    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()  # プログラム終了させるために必要

    logging.debug("longgggggggggggggggggggggggggg")
    logging.debug("end")


def worker2(queue):
    logging.debug("start")
    time.sleep(5)
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug("end")


if __name__ == "__main__":
    # queue でスレッド間のデータの受け渡しが可能
    queue = queue.Queue()
    for i in range(1000):  # mainスレッドで複数回処理追えたら次を行う
        queue.put(i)

    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue,))
        t.start()
        ts.append(t)

    logging.debug("tasks are not done")
    queue.join()
    logging.debug("tasks are done")

    for _ in range(len(ts)):
        queue.put(None)  # Noneを最後に入れないとwhile無限ループ

    [t.join() for t in ts]
# log
