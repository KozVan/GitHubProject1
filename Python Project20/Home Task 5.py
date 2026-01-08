print('How much numbers will it be?')
number = int(input())
print('Type', number, 'numbers')
spisok = list()
for i in range(0, number):
    spisok.append(int(input()))
spisok2 = spisok.copy()
spisok.remove(max(spisok))

while True:
    if max(spisok) == max(spisok2):
        spisok.remove(max(spisok))
    else:
        break

max1 = max(spisok)
max2 = max(spisok2)
print(max2, max1)