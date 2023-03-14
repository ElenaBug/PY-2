

def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал не должен считаться от отрицательного числа")
    if n == 0:
        return 1
    spisok = [i+1 for i in range(n)]
    a = 1
    for i in spisok:
        a *= i
    return a


if __name__ == '__main__':
    print(factorial_iterative(6))
