def args_kwagrs(*args, **kwargs):
    """Функцию с args и kwargs"""
    for arg in args:
        print(f"This is arg: {arg}")
    for key, value in kwargs.items():
        print(f"This is kwarg key: {key}")
        print(f"This is kwarg value: {value}")


if __name__ == "__main__":
    args_kwagrs("hello", "world", kwarg_1="hello", kwarg_2="world")
