"""
Задание 1

Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
 “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
 dignissim vitae libero” и после этого выводит получившийся текст на экран.
 Знаки препинания не должны оказаться внутри слова.
 Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
 но уже преобразованного.

"""
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()

for i in range(len(words)):
    if words[i][-1] in [',', '.']:
        words[i] = words[i][:-1] + 'ing' + words[i][-1]
    else:
        words[i] += 'ing'

result = ' '.join(words)
print(result)
