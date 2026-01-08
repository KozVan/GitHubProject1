num_str = input()
spisok = [int(num_str[0]), int(num_str[1]), int(num_str[2])]
max_num = max(spisok)
min_num = min(spisok)
spisok.remove(max_num)
spisok.remove(min_num)
other_num = spisok[0]
if max_num - min_num == other_num:
    print('Interesting number')
else:
    print('Not interesting number')

# num = int(input())
# aj = num // 100
# ag = (num % 100) // 10
# af = num % 10
# spisok = [aj, ag, af]
# max_num = max(spisok)
# min_num = min(spisok)
# spisok.remove(max_num)
# spisok.remove(min_num)
# other_num = spisok[0]
# if max_num - min_num == other_num:
#     print('Interesting number')
# else:
#     print('Not interesting number')
