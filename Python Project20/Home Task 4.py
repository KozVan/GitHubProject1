# num1 = int(input())
# num2 = int(input())
# for i in range(num1, num2 + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

num1 = int(input())
num2 = int(input())
listok = list(range(num1, num2 + 1))
for i in range(len(listok)):
    if listok[i] % 10 == 9:
        print(listok[i])