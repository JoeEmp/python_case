from locust import HttpUser, TaskSet, task
import random
import os
import requests


class WebsiteTasks(TaskSet):
    def on_start(self, token=''):
        self.token = token or 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjYyMDI4MDAsImlhdCI6MTYyNjEyODQ1MCwidXNlcl9pZCI6IjVhMzFlYmUxZGUxOGUyMDAwMTU4MmYwMiIsImxvZ2luX3NvdXJjZSI6MX0.1ZmniDMIqxEltQwxKfe50lzkLyadOAxJYkY3AHduOHs'

    @task
    def lottery(self):
        self.client.post(
            '/gorilla/api/v2.0/business-competition/lottery',
            headers={
                'authorization': 'gorilla %s' % self.token,
                'Content-Type': 'application/json'
            },
            verify=False
        )


class WebsiteUser(HttpUser):
    env = 'test'
    tasks = [WebsiteTasks]
    host = "https://%sop.xhwx100.com" % env
    min_wait = 1000
    max_wait = 5000


if __name__ == "__main__":
    import os
    os.system('python3 -m locust -f %s' % __file__)
