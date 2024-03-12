"""
Задание 2

Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция

Код, использующий этот декоратор может выглядеть, например, так:

@repeat_me
def example(text):
    print(text)

example('print me', count=2)
В результате работы будет такое:

print me

print me

"""


def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.get('count', 1)
        for _ in range(count):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
