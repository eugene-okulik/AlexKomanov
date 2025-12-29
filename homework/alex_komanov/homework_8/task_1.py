import random

salary = int(input("Enter your salary: "))
bonus = bool(random.randint(0, 1))  # OR bonus = random.choice([True, False])

total_salary = salary

if bonus:
    total_salary = salary + random.randint(1, salary)

print(f"Результат: {salary}, {bonus} - '{total_salary = }$'")
