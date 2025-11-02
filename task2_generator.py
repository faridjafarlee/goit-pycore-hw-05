import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел, відокремлених пробілами
    # \b - межа слова, \d+ - одна або більше цифр, \.? - опціональна крапка
    # \d* - нуль або більше цифр після крапки
    pattern = r'\b\d+\.\d+\b|\b\d+\b'
    
    # Знаходимо всі числа у тексті
    matches = re.findall(pattern, text)
    
    # Повертаємо кожне знайдене число як float
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
