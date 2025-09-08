import random
import string
import time
from typing import Dict
import matplotlib.pyplot as plt

# O(n)
def count_letters_horoshi_sposob(string) -> str:
    letters_count = {}
    for letter in string:
        letters_count[letter] = letters_count.get(letter, 0) + 1

    return max(letters_count.items(), key=lambda x: x[1])[0]

#O(n^2)
def count_letters_tupoy_sposob(string) -> str:
    max_letter = ''
    max_count = 0
    for letter in string:
        quantity = string.count(letter)
        if quantity > max_count:
            max_count = quantity
            max_letter = letter
    return max_letter

def generate_test_data(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def benchmark_algorithms():
    sizes = [100, 1000, 5000, 10000, 50000, 100000]
    times_horoshi = []
    times_tupoy = []

    for size in sizes:
        test_string = generate_test_data(size)

        start_time = time.time()
        count_letters_horoshi_sposob(test_string)
        dict_time = time.time() - start_time
        times_horoshi.append(dict_time)

        start_time = time.time()
        count_letters_tupoy_sposob(test_string)
        counter_time = time.time() - start_time
        times_tupoy.append(counter_time)

    plt.figure(figsize=(12, 6))

    plt.plot(sizes, times_horoshi, 'o-', label='Хороший алгоритм', linewidth=2)
    plt.plot(sizes, times_tupoy, 's-', label='Глупый алгоритм', linewidth=2)

    plt.xlabel('Длина строки')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение производительности алгоритмов')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')

    plt.tight_layout()
    plt.show()

benchmark_algorithms()