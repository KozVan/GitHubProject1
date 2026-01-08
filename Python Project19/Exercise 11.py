numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]  # Удаляем элемент имеющий индекс 5 (+1 к индексу)

print(numbers)


names = ['Gvido', 'Roman', 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef') # Подставляем элемент имеющий индекс 3 (+1 к индексу)
print(names)



names1 = ['Gvido', 'Roman', 'Timur']
position = names1.index('Timur')
print(position)
# position = names1.index('Anders')
# print(position)



food = ['rice', 'chicken', 'fish', 'brussel cabbage', 'rice']
print(food)
food.remove('rice')
print(food)



names2 = ['Gvido', 'Roman', 'Timur']
item = names2.pop(1)
print(item)
print(names2)



names3 = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names3.count('Timur')
cnt2 = names3.count('Gvido')
cnt3 = names3.count('Josef')

print(cnt1, cnt2, cnt3, sep='\n')



names4 = ['Gvido', 'Roman', 'Timur']
names4.reverse()
print(names4)



names5 = ['Gvido', 'Roman', 'Timur']
names5.clear()
print(names5)



names6 = ['Gvido', 'Roman', 'Timur']
names6_copy = names6.copy()

print(names6)
print(names6_copy)



a = [4, 4535, 4535346346, 6264274742, 7, 1571, 375, 8, 17813578, 3831, 81, 47, 36, 31, -7, -1, 67, 6767, 676767, 67676767, 6767676767, 676767676767, 67676767676767, 6767676767676767]
a.sort()

print('Отсортированный список:', a)