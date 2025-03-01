def process_line(line: str) -> int:
    """
    Извлекает число из строки, прибавляет 10 и возвращает результат.
    """
    parts = line.split(':')
    return int(parts[-1].strip()) + 10

# Список строк с результатами
results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result_line in results:
    print(process_line(result_line))
