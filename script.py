def factores(n):
    if n%15==0:
        print("Divisible entre 3 y 5")
    elif n%3==0:
        print("Divisible entre 3")
    elif n%5 == 0:
        print("Divisible entre 5")
    else:
        print(n)


num = int(input("Da un entero: "))
factores(num)

print('Goodbye')
