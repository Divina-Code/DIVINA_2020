"""
HOMEWORK
ИГРА- УГАДАЙ ЧИСЛО
компьютер загадывает любое число (от 1 до 100)
в ЦИКЛЕ спрашиваем пользователя и говорим, его догадка БОЛЬШЕ, МЕНЬШЕ или РАВНА загаданному компьютером чилу.
Когда число угадано - игра завершается


"""
from random import randint
from time import sleep


computer_number = randint(0, 100)

isGuessed = False
lives = 10

while not isGuessed and lives>0:
    answer = int(input("Назови число от 1 до 100: "))
    # lives = lives - 1
    lives -= 1


    if answer == computer_number:
        print("you win")
        isGuessed = True
    elif answer > computer_number:
        print("Too big number")
    else:
        print("Too small")

    sleep(1)

print("game over")
