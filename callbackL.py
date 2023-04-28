import time


def appy_async(func, args, callback):
    result = func(*args)
    reason = 7
    callback(reason)

def add(x ,y):
    time.sleep(5)
    print("WHY IS ASYNC")
    return x + y

class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handle(self, result):
        self.sequence += 1
        print("[{}] Got: {}".format(self.sequence, result))

r = ResultHandler()
appy_async(add, (2,3), callback=r.handle)