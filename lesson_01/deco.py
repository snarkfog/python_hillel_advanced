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


# Homework 1. Cache function (update)
def cache(max_limit=float("inf")):
    def limit(f):
        @wraps(f)
        def deco(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))
            if key in deco._cache:
                return deco._cache[key]

            if len(deco._cache) == max_limit:
                deco._cache.pop(next(iter(deco._cache)))

            result = f(*args, **kwargs)
            deco._cache[key] = result
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
