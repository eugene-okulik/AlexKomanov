# Программа "Угадайка"

target = 7  # Можно изменить на любое другое число

while True:
    try:
        guess = int(input("Угадайте цифру: "))
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        continue
    if guess == target:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
