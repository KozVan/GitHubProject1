num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break
if flag == True:
    print('Простое число')
else:
    print('Составное число')