from queue import Queue


class api_queue():
    def __init__(self, max_size=10):
        self.queue = Queue(max_size)

    def __len__(self):
        return self.queue.qsize()

    def put(self, func, *args, **kwargs):
        block = kwargs.pop("block", True)
        timeout = kwargs.pop("timeout", None)
        self.queue.put((func, args, kwargs), block=block, timeout=None)

    def get(self, *args, **kwargs):
        func, args, kwargs = self.queue.get(*args, **kwargs)
        return func(*args, **kwargs)

    def full(self):
        return self.queue.full()

    def empty(self):
        return self.queue.empty()
