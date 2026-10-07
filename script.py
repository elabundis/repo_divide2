num = int(input("Da un entero: "))

if num%15==0:
    print("Divisible entre 3 y 5")
elif num%3==0:
    print("Divisible entre 3")
elif num%5 == 0:
    print("Divisible entre 5")
else:
    print(num)

print('Goodbye')
