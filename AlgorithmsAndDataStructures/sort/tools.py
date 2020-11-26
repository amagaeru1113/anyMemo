from functools import wraps
import time

# ref https://qiita.com/hisatoshi/items/7354c76a4412dffc4fd7

def stop_watch(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        elapsed_time = time.time() - start
        print('{} : {:.5f} sec'.format(f.__name__, elapsed_time))
        return result
    return wrapper


if __name__ == '__main__':
    @stop_watch
    def _func():
        time.sleep(2)
        print('1')

    _func()