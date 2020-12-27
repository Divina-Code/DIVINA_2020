"""
Узнать у пользователя его имя и год рождения
посчитать его возраст
ЕСЛИ пользователю больше 18 лет, предложить ему посмотреть боевик
ИНАЧЕ предложить ему комедию

"""

user_name = input("What is your name    ")
user_year = int(input("when you was born    "))

if 2020 - user_year >= 18:
    print(user_name+', you can watch a action movie')
elif 2020 - user_year >= 16 :
    print(user_name+', you can watch a horror movie')
elif 2020 - user_year >= 13 :
    print(user_name+', you can watch a comedy movie')
else:
    print(user_name+', you can watch a cartoon')




