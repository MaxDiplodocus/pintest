import random

print("Загадайте число от 1 до 100, а я попробую его угадать!")
input("Нажмите Enter, когда будете готовы...")

low = 1
high = 100
attempts = 0

while True:
    attempts += 1
    guess = random.randint(low, high)
    print(f"Я думаю, это {guess}.")
    
    response = input("Это число больше (>), меньше (<) или равно (=) вашему? ").strip()
    
    if response == "=":
        print(f"Ура! Я угадал число {guess} за {attempts} попыток!")
        break
    elif response == ">":
        low = guess + 1
    elif response == "<":
        high = guess - 1
    else:
        print("Непонятный ответ. Пожалуйста, используйте только >, < или =.")
