# text = input()
# print(text.count('1' and '2'))
text = input()
a1 = 0
for i in range(0, 10):
    a1 = a1 + text.count(str(i))
print(a1)