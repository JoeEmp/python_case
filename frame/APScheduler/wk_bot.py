import requests
from selenium import webdriver
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import sys


config_data = {
    # 提测时间
    "test_dealine": "2019-07-12 13:30:00",
    # 机器人的key
    "test_key": 'f6447e4d-6101-4e7b-a971-2560c42aeb53'
}


def send_msg(content, phone_list):
    bot_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s' % config_data['test_key']
    text_json = {
        "msgtype": "text",
        "text": {
            "content": content,
            "mentioned_mobile_list": phone_list
        }
    }
    # markdown_data={}
    r = requests.post(url=bot_url, json=text_json)
    print(r.json())


def job():
    # 对输入的内容格式做处理
    try:
        if len(config_data['test_dealine']) < 10:
            print('时间格式有误，应为 2019-07-12 或 2019-07-12 00:00:00')
            scheduler.shutdown(wait=False)
            exit(0)
        test_dealine = datetime.datetime.strptime(
            config_data["test_dealine"], "%Y-%m-%d %H:%M:%S")
    except:
        test_dealine = datetime.datetime.strptime(
            config_data["test_dealine"]+" 00:00:00", "%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    days = (now-test_dealine).days
    # 项目组人员的电话号码
    phone_list = [
        '15521245028',  #兆聪
        '17777826220',  #光明
        '13922455242',  #晓令
        '15692003859'   #俊成
    ]
    content = 'init'
    # 提醒规则请自定义
    if days == 1:
        content = "各位开发大佬，我是本群的提测小助手\n明天(%s)就要提测了，请控制好项目进度" % config_data['test_dealine'].split(
            ' ')[0]
        send_msg(content, phone_list)
        # print(phone_list)
    elif days == 0:
        content = "各位开发大佬，我是本群的提测小助手\n今天(%s)就要提测了，如未提测请尽早完成，辛苦了" % config_data['test_dealine'].split(
            ' ')[0]
        send_msg(content, phone_list)
        # print(phone_list)
        scheduler.shutdown(wait=False)
        exit(0)
    elif days < 0:
        scheduler.shutdown(wait=False)
        exit(0)
    print(content)


if __name__ == "__main__":
    # BlockingScheduler
    try:
        config_data['test_dealine'] = sys.argv[1]
    except IndexError:
        pass
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='1-5',
                      hour=9, minute=40, second=20)
    scheduler.start()


'''
curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f6447e4d-6101-4e7b-a971-2560c42aeb53' \
   -H 'Content-Type: application/json' \
   -d '
   {
        "msgtype": "text",
        "text": {
            "content": "hello world"
        }
   }'
'''
