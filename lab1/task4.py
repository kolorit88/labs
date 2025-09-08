import time
import matplotlib.pyplot as plt

def del_time(data_structure, size):
    if isinstance(data_structure, dict):
        test_dict = {i: i for i in range(size)}
        start = time.time()
        for i in range(size):
            del test_dict[i]
        end = time.time()
    else:
        test_list = list(range(size))
        start = time.time()
        for i in range(size-1, -1, -1):
            del test_list[i]
        end = time.time()
    return end - start

sizes = [10_000, 100_000, 1_000_000, 2_000_000, 3_000_000, 5_000_000, 10_000_000,
         20_000_000, 40_000_000, 45_000_000]
dict_times = []
list_times = []

for size in sizes:
    dict_time = del_time(dict(), size)
    list_time = del_time(list(), size)
    dict_times.append(dict_time)
    list_times.append(list_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, dict_times, label='Dictionary', marker='o')
plt.plot(sizes, list_times, label='List', marker='s')
plt.xlabel('Кол-во элементов')
plt.ylabel('Время(секунды)')
plt.title('del операция')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()