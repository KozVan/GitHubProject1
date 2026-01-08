num = -int(input())
num1 = -int(input())
stars = '*'
for num1 in range(num - 1, 1):
    for j in range(-num1 - 1):
        print(stars, end=' ')
    print()                         # but it's possible to do with only one equal of x (но это возможно с одной переменной)