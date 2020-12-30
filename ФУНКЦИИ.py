



number = 100



def factorial(number):
    fact = 1
    for a in range(1, number+1):
        fact*=a

    return fact



print(factorial(10))
print(factorial(8))
print(factorial(5))
