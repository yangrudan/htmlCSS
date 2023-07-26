import logging
import psutil
import time


def get_process():
    result = []
    process_list = []
    pid = psutil.pids()

    for k,i in enumerate(pid):
        try:
            prco = psutil.Process(i)
            ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(prco.create_time()))
            process_list.append((str(i), prco.name(), prco.cpu_percent(), prco.memory_percent(), ctime))
        except psutil.NoSuchProcess as e:
            logging.error("psutil.NoSuchProcess" + str(e))

        process_list.sort(key=lambda x: x[3], reverse=True)

    for i in process_list:
        dict = {"PID": i[0], "name": i[1], "cpu": i[2], "mem": "%.2f%%" % i[3], "ctime":i[4]}
        result.append(dict)

    print(result)

while 1:
    get_process()
    time.sleep(1)
