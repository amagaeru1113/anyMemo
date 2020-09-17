import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(x, y=1):
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def worker2():
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")


if __name__ == "__main__":
    # N 秒後に始める設定
    t = threading.Timer(3, worker1, args=(100,), kwargs={"y": 200})
    t.start()

    # t1 = threading.Thread(target=worker1)
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()

    # print("started")
    # t1.join()  # プログラムを強制的に終了させない setDaemonより強い ソンビにさせないために設定するのが無難
    # t2.join()

