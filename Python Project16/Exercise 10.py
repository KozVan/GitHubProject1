text = input()
flag= True
for i in range(0, len(text)):
    c = text[i]
    if c in '0123456789':
        flag=False
if flag==True:
    print('no')
else:
    print('yes')