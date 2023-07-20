import psutil
import time


while 1:
  pids = psutil.pids()
  for pid in pids:
      p = psutil.Process(pid)
      print(f'进程号：{pid}，进程名：{p.name()}')
  print("================================================")
  time.sleep(5)