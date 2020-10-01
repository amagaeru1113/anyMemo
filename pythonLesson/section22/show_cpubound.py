import concurrent.futures
import os
import time

LEARGE_TEXT = "some string" * 1000000


def cpu_bound():
    i = 0
    while i < 10000000:
        i = i + 1 - 2 + 3 - 4 + 5
    return "Future is done."


if __name__ == "__main__":
    start = time.time()
    print(cpu_bound())
    print(cpu_bound())
    end = time.time()
    print("I/O bound sync {:.4f}\n".format(end - start))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executer:
        start = time.time()
        future1 = executer.submit(cpu_bound)
        future2 = executer.submit(cpu_bound)
        print(future1.result())
        print(future2.result())
        end = time.time()
        print("I/O bound sync {:.4f}\n".format(end - start))

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executer:
        start = time.time()
        future1 = executer.submit(cpu_bound)
        future2 = executer.submit(cpu_bound)
        print(future1.result())
        print(future2.result())
        end = time.time()
        print("The number of cpu: {}".format(os.cpu_count()))
        print("I/O bound process {:.4f}\n".format(end - start))

# log
# Future is done.
# Future is done.
# I/O bound sync 1.5063

# Future is done.
# Future is done.
# I/O bound sync 1.6265

# Future is done.
# Future is done.
# The number of cpu: 4
# I/O bound process 0.8179
