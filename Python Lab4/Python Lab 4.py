#print('Какой язык программирования мы изучаем?')
#answer = input()
#if answer == 'Python':
#    print('Верно! Мы ботаем Python =)')
#    print('Python - отличный язык')
#else:
#    print('Не совсем так!(')
#num1 = int(input())
#num2 = int(input())

#if num1 < num2:
#    print(num1, 'меньше чем', num2)

#if num1 > num2:
#    print(num1, 'больше чем', num2)

#if num1 == num2:
#    print(num1, 'равно', num2)

#if num1 != num2:
#    print(num1, 'не равно', num2)
#age = int(input())
#if 3 <= age <= 6:
#    print('Вы ребенок')
#else:
#    print('Вы не ребенок')
#a = int(input())
#b = int(input())
#c = int(input())
#if a == b == c:
#    print('числа равны')
#else:
#    print('числа не равны')
#x = input()
#if x == 'Python':
#    print('Da')
#else:
#    print('Net')
#a = int(input())
#b = a % 10
#c = a // 10
#d = (a // 10) % 10
#if b == c == d:
#    print('da')
#else:
#    print('net')
#x = int(input())
#y = x // 10
#z = x % 10
#t = (x // 10) % 10
#c = 0
#v = 0
#b = 0
#if y == (2, 4, 6, 8, 10, 12, 14, 16, 18, 20):
#    c = 1
#if z == (2, 4, 6, 8, 10, 12, 14, 16, 18, 20):
#    v = 1
#if t == (2, 4, 6, 8, 10, 12, 14, 16, 18, 20):
#    b = 1
#n = c + v + b
#print(n)
#x = int(input())
#y = int(input())
#z = int(input())
#count = 0 # chetchik
#
#if x % 2 == 0:
#    count = count + 1
#if y % 2 == 0:
#    count = count + 1
#if z % 2 == 0:
#    count = count + 1
#print(count)
#password = input()
#if password == 'qwerty':
#    print('Password is correct')
#else:
#    print('Password is uncorrect')
#agenumber = int(input())
#if agenumber < 18:
#    print('You cant enter this sie (go to main menu of browser)')
#
#if agenumber < 0:
#    print('Error')
#
#else:
#    print('You can enter this site (enter)')
#num1 = int(input())
#num2 = int(input())
#num3 = int(input())
#if num1 < num2:
#    print(num1, '<', num2)
#if num2 < num3:
#    print(num2, '<', num3)
#if num2 < num1:
#    print(num2, '<', num1)
#if num3 < num2:
#    print(num3, '<', num2)
#if num1 < num3:
#    print(num1, '<', num3)
#if num3 < num1:
#    print(num3, '<', num1)
human = int(input())
if human < 13:
    print('Youre a kid')
if human < 24:
    print('Youre a teen')
if human == 24:
    print('Youre a teen')
if human == 13:
    print('Youre a kid')
if human > 24:
    print('Youre a parent')
if human == 59:
    print('Youre a parent')
if human > 60:
    print('Youre old')