import pync
from playsound import playsound
import os
from threading import Thread


def sound(sound_file):
    playsound(sound_file)


def my_notify(*args, **kwargs):
    if kwargs.get('sound', None):
        sound_file = kwargs['sound']
        kwargs.pop('sound')
    t = Thread(target=sound, args=(sound_file,))
    t.start()
    pync.notify(*args, **kwargs)


if __name__ == "__main__":
    my_notify('123', title='this is title', sound="wechat_tips.mp3")