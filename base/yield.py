#!/usr/bin/env python3

from time import time as current_time
from random import random as rd

#range函数的实现
def my_range(start,stop=0,step=1):
    if stop < start:
        t,stop,start = stop,start,t
    while start < stop:
        start += step
        yield start-1

events_list = list()

class Event(object):
    def __init__(self, *args, **kwargs):
        events_list.append(self)
        self._callback = lambda:None
    def is_ready(self):
        ready = self._is_ready()
        if ready:
            self._callback()
        return ready
    def set_callback(self, callback):
        self._callback = callback

class SleepEvent(Event):
    def __init__(self, duration):
        super(SleepEvent, self).__init__(duration)
        self._duration = 2 * rd() * duration
        self._start_time = current_time()
    def _is_ready(self):
        return (current_time() - self._start_time >= self._duration)

class Dispatcher(object):
    def __init__(self, tasks):
        self.tasks = tasks
        self._start()
    def _next(self, gen_task):
        try:
            yielded_event = next(gen_task)
            yielded_event.set_callback(lambda: self._next(gen_task))
        except StopIteration:
            pass
    def _start(self):
        for task in self.tasks:
            self._next(task)
    def polling(self):
        while len(events_list):
            for event in events_list:
                if event.is_ready():
                    events_list.remove(event)
                    break

def coroutine_sleep(duration):
    return SleepEvent(duration)

def greeting(name, times, duration = 1):
    for i in range(times):
        yield coroutine_sleep(duration)
        print("Hello, %s.%d!" % (name, i))

if __name__ == '__main__':
    print(dir(my_range))
    # def test():
    #     dispatcher = Dispatcher([greeting('Liam', 3), greeting('Sophia', 3), greeting('Cancan', 3)])
    #     dispatcher.polling()

    # import timeit
    # timeit_times = 10
    # avg_cost = timeit.timeit(lambda: test(), number = timeit_times) / timeit_times
    # print('%.3f' % (avg_cost))