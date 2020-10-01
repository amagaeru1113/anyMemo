import concurrent.futures
import os
import time

LEARGE_TEXT = "some string" * 10000000


def io_bound(file_name):
    with open(file_name, "w+") as f:
        f.write(LEARGE_TEXT)
        f.seek(0)
        f.read()

    os.remove(file_name)
    return "Future is done."


def cpu_bound():
    i = 0
    while 1 < 10000000:
        i = i + 1 - 2 + 3 - 4 + 5
    return "Future is done."


if __name__ == "__main__":
    start = time.time()
    print(io_bound("1.txt"))
    print(io_bound("2.txt"))
    end = time.time()
    print("I/O bound sync {:.4f}\n".format(end - start))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executer:
        start = time.time()
        future1 = executer.submit(io_bound, "1.txt")
        future2 = executer.submit(io_bound, "2.txt")
        print(future1.result())
        print(future2.result())
        end = time.time()
        print("I/O bound sync {:.4f}\n".format(end - start))

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executer:
        start = time.time()
        future1 = executer.submit(io_bound, "1.txt")
        future2 = executer.submit(io_bound, "2.txt")
        print(future1.result())
        print(future2.result())
        end = time.time()
        print("The number of cpu: {}".format(os.cpu_count()))
        print("I/O bound process {:.4f}\n".format(end - start))

# log
# Future is done.
# Future is done.
# I/O bound sync 1.6072

# Future is done.
# Future is done.
# I/O bound sync 1.2309

# Future is done.
# Future is done.
# The number of cpu: 4
# I/O bound process 1.1193
