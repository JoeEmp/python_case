<!--
 * @Author: your name
 * @Date: 2020-03-18 23:01:50
 * @LastEditTime: 2020-03-18 23:02:05
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /learn_case/frame/notion/notion.md
 -->


## python
- 气泡提醒

气泡提醒对比自己写的样式提醒更加和谐，但是需要针对平台去做适配，按需使用。windows没有但是有系统托盘提醒

mac:pync&emsp;linux:pynotify

```python
# simple demo
import pync
if __name__ == "main":
    pync.notify(title="title",message="message")
```

windows附个码
```python
# -*- encoding: utf-8 -*-
import uuid
from win32api import *
from win32gui import *
import win32con
import  os
import time
 
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
 
'''windows托盘提醒'''
class WindowsBalloonTip:
    executor=ThreadPoolExecutor(10)
    @run_on_executor
    def alert(self, title, msg,delay=1):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = str(uuid.uuid1())
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(classAtom, "Taskbar", style, \
                                 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                                 0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.dirname(os.path.abspath('.'))+'\\logo.ico'
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = LoadImage(hinst, iconPathName, \
                              win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, \
                          hicon, "Balloon  tooltip", title, 200, msg))
        '''延时几秒后销毁消息及托盘图标'''
        time.sleep(delay)
        DestroyWindow(self.hwnd)
 
    @run_on_executor
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)  # Terminate the app.
 
windows_alert=WindowsBalloonTip()
# def balloon_tip(title, msg):
#     w = WindowsBalloonTip(msg, title)
 
if __name__ == '__main__':
    windows_alert.alert(u'提醒',u'what are you 弄撒咧.')
```