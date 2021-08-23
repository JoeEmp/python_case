from app import sendmail
from time import sleep
result = sendmail.delay(dict(to='celery@python.org'))
print(dir(result))
while not result.ready():
    print('task running')
    sleep(1)
print('task done')