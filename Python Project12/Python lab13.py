# n % 10 - types last number
# n // 10 - number with further from last number (deletes last number)
n = int(input())
while n != 0:
    last_digit = n % 10
    n = n // 10