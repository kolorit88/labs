import sys
import time
from random import randrange
from typing import Callable, List
import matplotlib.pyplot as plt
from matplotlib.pyplot import title

sys.setrecursionlimit(100000)

def swap(arr, a, b):
    """ переставляем элементы a и b в массиве """
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(unsorted, start, end):
    """ arrange (left array < pivot) and (right array > pivot) """

    # выбираем значение pivot как последний элемент неотсортированного сегмента
    pivot = unsorted[end]

    # назначаем на pivot значение левого индекса
    i_pivot = start

    # проходим от начала до конца текущего сегмента
    for i in range(start, end):

        # сравниваем текущее значение со значением pivot
        if unsorted[i] <= pivot:

            # меняем местами текущее значение и значенрие pivot
            swap(unsorted, i, i_pivot)

            # увеличиваем значение пивота
            i_pivot += 1

    # ставим пивот в правильную позицию, заменив со значением слева
    swap(unsorted, i_pivot, end)

    # возвращаем следующее значение пивота
    return i_pivot

def measure_time(sort_func: Callable, arr: List[int]) -> float:
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def quick_sort(unsorted, start=0, end=None):
    """ быстрая сортировка """
    if end is None:
        end = len(unsorted) - 1

    # останавливаемся, когда индекс слева достиг или превысил индек справа
    if start >= end:
        return

    # определяем позицию следующего пивота
    i_pivot = partition(unsorted, start, end - 1)

    # рекурсивный вызов левой части
    quick_sort(unsorted, start, i_pivot - 1)

    # рекурсивный вызов правой части
    quick_sort(unsorted, i_pivot + 1, end)


def selection_sort(unsorted):
    # итерируемся по массиву
    n = len(unsorted)
    for i in range(0, n):

        # инициализируемся первым значеним
        current_min = unsorted[i]

        # инициализируем минимальный индекс
        min_index = i

        # итерируемся по оставшимся элементам массива
        for j in range(i, n):

            # проверяем, если j-тое значение меньше текушего минимального
            if unsorted[j] < current_min:
                # обновляес минимальные значение и индекс
                current_min = unsorted[j]
                min_index = j

        # меняем i-тое и j-тое значения
        swap(unsorted, i, min_index)

def generate_random_arr(size):
    return [randrange(0, size) for _ in range(size)]

sizes_for_test = [1000, 2000, 3000, 4000, 5000, 6000]
times_quick_sort_random = []
times_select_sort_random = []

times_quick_sort_sorted = []
times_select_sort_sorted = []

times_quick_sort_sorted_rev = []
times_select_sort_sorted_rev = []

for size in sizes_for_test:
    arr = generate_random_arr(size)
    arr_sorted = sorted(arr)
    arr_sorted_rev = arr_sorted[::-1]

    times_select_sort_random.append(measure_time(selection_sort, arr.copy()))
    times_quick_sort_random.append(measure_time(quick_sort, arr.copy()))

    times_select_sort_sorted.append(measure_time(selection_sort, arr_sorted.copy()))
    times_quick_sort_sorted.append(measure_time(quick_sort, arr_sorted.copy()))

    times_select_sort_sorted_rev.append(measure_time(selection_sort, arr_sorted_rev.copy()))
    times_quick_sort_sorted_rev.append(measure_time(quick_sort, arr_sorted_rev.copy()))

print(times_select_sort_random)
print(times_quick_sort_random)

plt.figure(figsize=(10, 8))
plt.title('random')
plt.plot(sizes_for_test, times_quick_sort_random, marker="o", label='quick_sort')
plt.plot(sizes_for_test, times_select_sort_random, marker="s", label='select_sort')
plt.show()

plt.figure(figsize=(10, 8))
plt.title('sorted')
plt.plot(sizes_for_test, times_quick_sort_sorted, marker="o", label='quick_sort')
plt.plot(sizes_for_test, times_select_sort_sorted, marker="s", label='select_sort')
plt.show()

plt.figure(figsize=(10, 8))
plt.title('sorted_rev')
plt.plot(sizes_for_test, times_quick_sort_sorted_rev, marker="o", label='quick_sort')
plt.plot(sizes_for_test, times_select_sort_sorted_rev, marker="s", label='select_sort')
plt.show()