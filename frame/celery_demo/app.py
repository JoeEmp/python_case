import time
from celery import Celery

app = Celery('tasks', broker='redis://:hmj12345@localhost:6379/0')
app.conf.broker_url = 'redis://:hmj12345@localhost:6379/0'
app.conf.result_backend = 'redis://:hmj12345@localhost:6379/0'

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(10.0)
    print('mail sent.')


if '__main__' in __name__:
    app.start()
