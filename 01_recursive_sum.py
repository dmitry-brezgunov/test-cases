def recursive_sum(array):
    """Рекурсивная функция сложения массива чисел"""
    if array:
        return array.pop() + recursive_sum(array)
    else:
        return 0


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    print(recursive_sum(array))
