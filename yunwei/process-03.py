import time

import psutil

def get_progress_pid():
    # 获取任务管理器所有的进程信息
    for p in psutil.process_iter():
        try:
            print('进程名称:', p.name())#显示进程名称
            print('进程运行命令', p.cmdline())#进程运行命令
            print('运行状态:', p.status()) #运行状态
            print('进程pid:', p.pid) #进程pid
            print('父进程pid:', p.ppid()) #父进程pid
            print('父进程:', p.parent()) #父进程
            print('进程bin路径:', p.exe()) #进程bin路径
            print('*'*100)
        except:
            pass

def judge_process_exist(pid=None, port=None):
    # 判断进程是否存在
    if not pid and port:
        port_pid = {}
        for i in psutil.net_connections():
            pid = i.pid
            status = i.status
            port = i.laddr.port
            port_pid[port] = pid
        pid = port_pid.get(port)

    if not pid:
        return
    # 判断进程id是否存在
    if pid in psutil.pids():
        p = psutil.Process(pid)
        return p.name()
    else:
        return None


def get_progress_chrome_path():
    # 获取进程中谷歌浏览器路径
    chrome_path = None
    for p in psutil.process_iter():
        if p.name().lower() == 'chrome.exe' and p.exe():
            chrome_path = p.exe()
            break
    return chrome_path


while 1:
    get_progress_pid()
    time.sleep(3)