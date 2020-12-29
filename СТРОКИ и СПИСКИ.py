
###КАК превратить СТРОКУ в СПИСОК элементов

shoppingList = input("Введи товары:\t")

print(len(shoppingList))
shoppingList = shoppingList.split(' ')
print(shoppingList)
print(len(shoppingList))



###Как из списка элементов сделать строку
myStudents = ["artem", "ilya", "ivan"]

print("My best students is:", ", ".join(myStudents))

