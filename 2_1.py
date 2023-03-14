import random
"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if len(arr) == 0:
        raise ValueError('Длина не должна быть нулевой')
    min_elem = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_elem:
            min_elem = arr[i]
    return min_elem


if __name__ == '__main__':
    print(min_search([1, 2, 5]))
    print(min_search([7, 1, -1, 3]))
