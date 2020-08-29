# 時間測定のデコレータ
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
        return result

    return wrapper


def say_twice(word):
    return (word + "!") * 2

