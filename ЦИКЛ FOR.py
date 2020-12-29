myStudents = ["artem", "ilya", "ivan"]



for student in myStudents:

    index = myStudents.index(student)
    myStudents[index] = student.title()

    # print(student, " Happy New Year")
print(myStudents)

myStudents = ["artem", "ilya", "ivan", 'ivan']

print("My best students is:", ", ".join(myStudents))

for student in myStudents:

    index = myStudents.index(student)
    myStudents[index] = student.title()

    # print(student, " Happy New Year")
print(myStudents)

# print(range(100))
# print(*range(100))
#
# print(*range(55, 78))
# print(*range(0, 1000, 29))


randomNumbers = [32, 84, 17, 66, 15, 89, 99]

for a in range(len(randomNumbers)):
    if a >0 and randomNumbers[a] > randomNumbers[a-1]:
        print(randomNumbers[a])




