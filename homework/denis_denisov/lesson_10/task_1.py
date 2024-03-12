"""
Задание 1

Создайте универсальный декоратор, который можно будет применить к любой функции.
Декоратор должен делать следующее: он должен распечатывать слово "finished" после выполнения декорированной функции.

Код, использующий этот декоратор может выглядеть, например, так:

@finish_me
def example(text):
    print(text)

example('print me')
В результате работы будет такое:

print me

finished

"""


def finish_me(func):


    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper

@finish_me
def example(text):
    print(text)

example('print me')
