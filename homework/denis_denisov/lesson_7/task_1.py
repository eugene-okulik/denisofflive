"""
Задание 1

Создайте такую программу:
Программа хранит какую-либо цифру в переменной.
Программа просит пользователя угадать цифру. Пользователь вводит цифру.
Программа сравнивает цифру с той, что хранится в переменной.
Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
Т.е. программа не завершается пока пользователь не угадает цифру.

Подсказка: задание выполняется с помощью цикла while

"""

number = 7

while True:
    guess = int(input("Угадайте цифру: "))
    if guess == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
