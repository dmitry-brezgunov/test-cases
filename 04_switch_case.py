class DayOfWeekSwitchCase:
    """Реалиазция switch-case для дней недели с использование классов."""
    def switch(self, day):
        """
        Основной метод. Принимает на вход число - день недели.
        Возвращает название недели, либо значение по умолчанию.
        """
        default = "Invalid day"
        return getattr(self, f"case_{day}", lambda: default)()

    def case_1(self):
        return "Monday"

    def case_2(self):
        return "Tuesday"

    def case_3(self):
        return "Wednesday"

    def case_4(self):
        return "Thursday"

    def case_5(self):
        return "Friday"

    def case_6(self):
        return "Saturday"

    def case_7(self):
        return "Sunday"


if __name__ == "__main__":
    value = int(input("Enter day number: "))
    day = DayOfWeekSwitchCase()
    print(day.switch(value))
