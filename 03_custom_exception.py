class NegativeIntegerException(Exception):
    """Кастомное исключение. Вызывается если целое число меньше 0."""
    def __init__(self, value):
        self.value = value
        self.message = f"{self.value} is less than 0"

    def __str__(self):
        return self.message


if __name__ == "__main__":
    x = int(input("Enter non negative number: "))
    if x < 0:
        raise NegativeIntegerException(x)
    else:
        print(x)
