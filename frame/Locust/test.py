import socket
import os
from urllib.parse import urlparse
import requests

CR_LF = '\r\n'

def get_requests_text(method, path, headers, body):
    global CR_LF
    # 请求行
    request_line = "%s %s HTTP/1.0%s" % (method, path, CR_LF)
    # 请求头
    request_header = CR_LF.join(
        [k+": "+v for k, v in headers.items()]) + CR_LF
    # 请求体
    request_body = CR_LF.join(
        [k+":"+v for k, v in body.items()]) + CR_LF
    return request_line + request_header + CR_LF + request_body

def sock_http_request(url, headers, body, method='POST'):
    _url = urlparse(url)
    hostname, port, path = _url.hostname, _url.port, _url.path
    request_text = get_requests_text(method, path, headers, body)
    if not port:
        port = 443 if url.startwith('https') else 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, port))
    print(request_text)
    sock.send(request_text.encode('utf-8')) # str to bytes 网络传输实际上都是二进制，所以要编码成二进制
    response = b''
    rec = sock.recv(1024)
    while rec:
        response += rec
        rec = sock.recv(1024)
    print(response.decode()) # bytes to str 同理为了方便我们阅读，则需要将二进制转会str
    return response.decode()

def good_list():
    # request 打印报文比较麻烦，这里只打印结果
    url = 'http://localhost:10086/jmeter/app/good/list'
    form = {"page": "1", "page_size": "1"}
    r = requests.post(url,data=form)
    print(r.text)


if "__main__" == __name__:
    url = 'http://localhost:10086/jmeter/app/good/list'
    headers = {"Host": 'localhost', "Connection": 'keep-alive'}
    body = {"page": "1", "page_size": "1"}
    sock_http_request(url, headers, body)
    good_list()