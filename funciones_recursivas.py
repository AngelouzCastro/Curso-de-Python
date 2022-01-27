#metodo resurcibo

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Booooooom!")

cuenta_atras(5)

#factorial
def factorial(num):
    print("valor",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final",num)
    return num

print(factorial(5))
