
isGuessed = False

while isGuessed != True:
    puzzle = "\nХоккеистов слышен плач \nПропустил вратарь их …"

    answer = input(puzzle)

    if answer == "шайбу":
        print("Дааа! ТЫ МОЛОДЕЦ!")
        isGuessed = True
    elif answer == "мяч":
        print("ПОПАЛСЯ! Не мяч)")
    else:
        print("Нет, не угадал, попробуй снова")

print("Спасибо за игру")

"""
Дать пользователю задачу с ЧИСЛОВЫМ ответом
Проверять ответы до тех пор, пока не будет введён правильный

"""
