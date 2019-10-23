import time



def during_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return result
    return wrapper

@during_time
def fun01():
    for i in range(10):
        pass

@during_time
def fun02():
    for i in range(10000):
        pass

fun01()
fun02()