"""
Пользователь за один инпут вводит вам разные слова
программа разделяет их на отдельные слова и проверяет, является ли слово палиндромом
Если является - выводит его нам


ВВЕДЕНО: шалаш,  казак, ракета
ВЫВОД: шалаш, казак

"""

words = input("Введите слова: ").lower().split()


palindroms = []
for word in words:
    if word == word[::-1]:
        # print(word)
        palindroms.append(word)

if len(palindroms)>0:
    print('ПАЛИНДРОМЫ: ', ", ".join(palindroms))
else:
    print("Тут нет палиндромов")
