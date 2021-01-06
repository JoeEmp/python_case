import requests
import threading


def async_rq(index):
    url = 'http://127.0.0.1:5000/queue/hello'
    r = requests.post(url, json={'name': '%d' % index})
    if r.json()['result'] != str(index):
        print(index, r.json())


if __name__ == "__main__":
    rqs=[]
    for i in range(100):
        rqs.append(threading.Thread(target=async_rq,args=(i,)))
    for t in rqs:
        t.start()
    for t in rqs:
        t.join()
    print("end")