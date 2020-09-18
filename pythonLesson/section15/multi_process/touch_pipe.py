import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def f(conn):
    conn.send(["test"])  # sendの時点でrecvされる
    time.sleep(5)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()  # 親から子に値を受けわたす
    p = multiprocessing.Process(target=f, args=(parent_conn,))
    p.start()
    # p.join() # 処理全体が終わるまで松-> 5秒松
    logging.debug(child_conn.recv())
