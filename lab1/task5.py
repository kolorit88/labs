import time
import matplotlib.pyplot as plt

def measure_in_time(data_structure, size, target):
    if isinstance(data_structure, set):
        test_set = set(range(size))
        start = time.time()
        for _ in range(100):
            target in test_set
        end = time.time()
    else:
        test_list = list(range(size))
        start = time.time()
        for _ in range(100):
            target in test_list
        end = time.time()
    return end - start

sizes = [10_000, 100_000, 1_000_000, 2_000_000, 3_000_000, 5_000_000]
set_times = []
list_times = []

for size in sizes:
    target = size + 1
    set_time = measure_in_time(set(), size, target)
    list_time = measure_in_time(list(), size, target)
    set_times.append(set_time)
    list_times.append(list_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, set_times, label='Set', marker='o')
plt.plot(sizes, list_times, label='List', marker='s')
plt.xlabel('Кол-во элементов')
plt.ylabel('Время(секунды)')
plt.title('In операция')
plt.legend()
plt.grid(True)
plt.show()