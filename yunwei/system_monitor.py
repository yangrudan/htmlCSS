import psutil

print(psutil.cpu_times())
print("--------------------------------")
print(psutil.cpu_times(percpu=True))
print("--------------------------------")
print(psutil.cpu_count())
print("--------------------------------")
print(psutil.cpu_count(logical=False))
print("--------------------------------")
print(psutil.cpu_percent())
print("--------------------------------")
print(psutil.cpu_percent(percpu=True))
print("--------------------------------")
print(psutil.virtual_memory())
print("--------------------------------")
print(psutil.disk_partitions())
print("--------------------------------")
print(psutil.net_if_addrs())

x = y =3
print("xx:", x is y)
x1 = x2 = [1.,2,3]
print(x1 is x2)
