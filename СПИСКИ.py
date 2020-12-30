
myDogs = []
myCats = ['Bonya', 'Bagira', 'Zelda', 'Zyza', 'Jenny', '56']
35

print( len(myCats))  ##Длина списка -- сколько элементов  в списке

print( sorted(myCats)) ## НЕ МЕНЯЕТ список, только возвращает сортированную копию
myCats.sort() ## СОРТИРУЕТ исходный спиок



myCats.append("Tom")  ###Добавить в конец
myCats.append("Katty") ###Добавить в конец
print(myCats)

myCats.pop(0)  #Удаление элемента по индексу
print(myCats)

print(myCats[5])  #Взять элемент с нужным индексом
print(myCats[-7]) #Взять элемент с конца

myCats+="Murzik"
print(myCats)
