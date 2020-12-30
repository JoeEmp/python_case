from locust import HttpUser, TaskSet, task
import random
import os
from utils import load_csv
from server import USER_TABLE

file_dir = os.path.abspath(os.path.dirname(__file__))+os.sep


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.data = load_csv(file_dir+'test_account.csv') + load_csv(file_dir+'locuts_account.csv')
        self.client.post("login", json=self.random_user())

    @task
    def index(self):
        self.client.get("")

    @task
    def about(self):
        self.client.get("about")

    def random_user(self):
        ret = random.choice(self.data)
        self.data.remove(ret)
        return ret


class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    host = "http://127.0.0.1:10086/"
    min_wait = 1000
    max_wait = 5000


if __name__ == "__main__":
    import os
    os.system('nohup python3 server.py &')
    os.system('python3 -m locust -f %s' % __file__)
