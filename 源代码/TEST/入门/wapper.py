import time


class ProcessTime:

    def __init__(self, func):
        print("coming ProcessTime __init__", id(self))
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        print("coming ProcessTime __call__, id(self.func) -->", id(self.func))
        ret = self.func(*args, **kwargs)
        end_time = time.time()
        print("ProcessTime 函数的执行时间为:%d" % (end_time - start_time))
        return ret


class ProcessTime2:

    def __init__(self, func):
        print("coming ProcessTime2 __init__", id(self))
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        print("coming ProcessTime2 __call__, id(self.func) -->", id(self.func))
        ret = self.func(*args, **kwargs)
        end_time = time.time()
        print("ProcessTime2 函数的执行时间为:%d" % (end_time - start_time))
        return ret


@ProcessTime
@ProcessTime2
def test(sleep_time):
    time.sleep(sleep_time)
    return "tet"


# test = ProcessTime2(test)
# test = ProcessTime(test)

t = test(1)