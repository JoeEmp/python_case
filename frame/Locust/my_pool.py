from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from utils import load_csv
import requests
import asyncio
import logging
import sys
import signal

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    filename='to_server.log'
)

max_workers = 1
thread_pool_executor = ThreadPoolExecutor(max_workers)
q = Queue(1000)


def login(username, password):
    logging.info('to server {} {}'.format(username, password))
    return requests.post('http://localhost:10086/login',
                         json={'username': username, 'password': password})


def prize_test(order_num):
    url = 'https://test-api.xhwx100.com/gorilla/api/v2.1/label/prize-test'
    headers = {
        "authorization": "gorilla eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjY0NjIwMDAsImlhdCI6MTYyNjQwMDkyMiwidXNlcl9pZCI6IjVhMzFlYmUxZGUxOGUyMDAwMTU4MmYwMiIsImxvZ2luX3NvdXJjZSI6MX0.gWCXjWtOXuHGBVCcPz8uCoKRgYbAKsRd-kaYlfVxbZk"
    }
    paylaod = {"order_num": order_num}
    r = requests.post(url, headers=headers, json=paylaod)
    logging.info("%s %s %s" % (r.status_code, r.text, paylaod))


def release(queue, func, num):
    for _ in range(num):
        thread_pool_executor.submit(func, **q.get())


def main():
    users = load_csv('locuts_account.csv')
    for i in range(len(users)):
        q.put(users[i])
        if q.qsize() >= max_workers:
            release(q, login, max_workers)


def main1():
    orders = [
        # '345771356790456321',
        # '345774311123976193',
        # '345782275385851905',
        '345771356673015809',
        '345770914291384321',
        '345770914274607105'
    ]
    for order in orders:
        q.put({'order_num': order})
        if q.qsize() >= max_workers:
            release(q, prize_test, max_workers)
    logging.info('-'*80)


main1()

# print(thread_pool_executor.submit.__doc__)
