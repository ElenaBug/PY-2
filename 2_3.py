A = 1
def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 0:
        return
    global A
    A *= n
    factorial_recursive(n-1)




if __name__ == '__main__':
    print(factorial_recursive(4))


print(A)
