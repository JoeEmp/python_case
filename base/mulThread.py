from threading import Thread
import threading
import requests
from abc import abstractmethod
from queue import Queue
import urllib3
urllib3.disable_warnings()

q = Queue()

class Producer():

    def __init__(self, q: Queue, items=None, time=0, item=None) -> None:
        self._q = q
        self.items = items or (item for _ in range(time))
        if isinstance(self.items, list):
            self.items = iter(self.items)

    @classmethod
    def simple_produce(cls, q, time, item):
        return cls(q, time=time, item=item)

    @classmethod
    def by_list(cls, q, items):
        return cls(q, items=items)

    def execute(self):
        count = 0
        while True:
            try:
                q.put(next(self.items))
                count += 1
            except StopIteration:
                break
        print(f'生产完成,生产总数为: {count}')


class Consumer():

    def __init__(self, q: Queue, max_executor: int) -> None:
        self._q = q
        self.max_executor = max_executor
        self.consumer_list = []

    @property
    def is_full(self):
        return self.max_executor <= len(self.consumer_list)

    def run(self):
        while True:
            if 0 == self._q.qsize() and 'ProducerThread' not in [t.getName() for t in threading.enumerate() if t.is_alive()]:
                print('已完成生产和消费,退出轮询消费')
                break
            # 线程已满
            if self.is_full:
                alive_consumer = [t for t in threading.enumerate(
                ) if t.is_alive() and 'MainThread' not in t.getName()]
                self.consumer_list = [ consumer for consumer in self.consumer_list if consumer in alive_consumer]
            elif self._q.qsize():
                item = self._q.get()
                t = Thread(target=self.execute,args=(item,))
                self.consumer_list.append(t)
                t.start()
        # 等待线程完成消费
        while True:
            alive_consumer = [t for t in threading.enumerate(
            ) if t.is_alive() and 'MainThread' not in t.getName()]
            if 0 == len(alive_consumer):
                break

    @abstractmethod
    def execute(self,item):
        pass


class RequestDemo(Consumer):
    def execute(self, item):
        response = requests.post(**item, proxies={
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }, verify=False)
        try:
            print(response.json())
        except Exception as e:
            print(response)
            print(response.text)

item={
    'url': 'http://127.0.0.1:5000/'
}

pt = Thread(target=Producer.simple_produce(q, 20,item).execute, name='ProducerThread')
pt.start()
RequestDemo(q, 4).run()
