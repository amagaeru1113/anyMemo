import logging
import threading
import time


logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1(d, lock):
    logging.debug("start")
    lock.acquire()  # lockする
    i = d["x"]
    time.sleep(5)
    d["x"] = i + 1
    logging.debug(d)
    lock.release()  # 開放する
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
    lock = threading.Lock()
    # t1 = threading.Thread(target=worker1, args=(d, ))  # sleep後にd['x'] = 1で上書きしてしまう
    # t2 = threading.Thread(target=worker2, args=(d, ))  # startしてd['x'] = 1にする

    # lockしているので、処理が終わってから次のthreadが動く
    t1 = threading.Thread(target=worker1, args=(d, lock))
    # lockしているので、d["x"]=1を取り出して処理をする
    t2 = threading.Thread(target=worker2, args=(d, lock))

    t1.start()
    t2.start()
