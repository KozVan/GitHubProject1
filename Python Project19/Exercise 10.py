numbers = [1, 2, 3]

numbers.append(10)
numbers.append(12)

print(numbers)



numbers1 = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers1.extend(odds)
print(numbers1)



words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')

print(words1)
print(words2)
