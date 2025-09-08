import matplotlib.pyplot as plt
import numpy as np
import time

sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 10000000]
times = []

def foo(nums):
    for x in nums:
        if x % 2 == 0:
            return True
    return False

for size in sizes:
    nums = list(range(1, size * 2 + 1, 2))

    start_time = time.time()
    foo(nums)
    end_time = time.time()

    times.append(end_time - start_time)


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, 'o-', linewidth=2, markersize=5)
plt.xlabel('Размер входных данных (n)')
plt.ylabel('Время выполнения (секунды)')
plt.title('Время выполнения функции foo(nums)')
plt.grid(True, alpha=0.3)
plt.show()
 # Сложность O(n)
 # Функция проверяет, есть ли в списке хотя бы одно четное число