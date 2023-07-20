import psutil

print(psutil.cpu_times())  # 统计 CPU 的用户／系统／空闲时间
print("--------------------------------")
print(psutil.cpu_times(percpu=True))
print("--------------------------------")
print(psutil.cpu_count())  # 获取 CPU 的逻辑核心数量
print("--------------------------------")
print(psutil.cpu_count(logical=False))  # 获取 CPU 的物理核心数量
print("--------------------------------")
print(psutil.cpu_percent())  # 查看 CPU 的使用率
print("--------------------------------")
print(psutil.cpu_percent(percpu=True))
print("--------------------------------")
print(psutil.virtual_memory())  # 查看内存使用情况
print("--------------------------------")
print(psutil.disk_partitions())  # 查看磁盘分区、磁盘使用率和磁盘 IO 信息
print("--------------------------------")
print(psutil.net_if_addrs())

