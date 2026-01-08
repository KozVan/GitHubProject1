n = int(input())
n1 = 0
for n1 in range(1, n + 1):
    minus = 0
    for j in range(n):
        minus +=1
        print(f'{n1 * minus:4}', end=' ')
    print()