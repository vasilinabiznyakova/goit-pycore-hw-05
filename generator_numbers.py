import re
from typing import Callable

def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total+=number

    return total

def generator_numbers(text):
    for match in re.findall(r'\d+(?:\.\d+)?', text):
        yield float(match)


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
assert round(total_income, 2) == 1351.46 # need round to compare float more strictly
print(f"Загальний дохід: {total_income}")
