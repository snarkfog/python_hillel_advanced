from time import time
from functools import wraps


def profile(msg="Elapsed time for function"):
    def internal(f):
        @wraps(f)
        def deco(*args, **kwargs):
            start = time()
            deco._num_call += 1
            result = f(*args, **kwargs)
            deco._num_call -= 1

            if deco._num_call == 0:
                print(msg, f'{f.__name__}: {time() - start}s')
            return result

        deco._num_call = 0
        return deco

    return internal


def cache(max_limit=None):
    def limit(f):
        @wraps(f)
        def deco(*args, **kwargs):
            if args in deco._cache:
                return deco._cache[args]

            if len(deco._cache) == max_limit:
                deco._cache.pop(next(iter(deco._cache)))

            result = f(*args, **kwargs)
            deco._cache[args] = result
            return result

        deco._cache = {}
        return deco

    return limit


@profile()
@cache(max_limit=64)
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(1000):
    print(i, '->', fibo(i))
