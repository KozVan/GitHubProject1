# num = int(input())
# total = 0
# while num != 0:
#     last_digit = num % 10 ( I need to write a code, that
#cymmiryet ego chifri, ymnozaet ego chifri, schitaet cpednee orifmiticheskoe chifp, pishet ego pervyi chifry i cymmipet pervoe i poslednee chislo
#     num = num // 10
#     print (last_digit)

num = int(input())
sum = 0
product = 1
count = 0
while num != 0:
    last_digit = num % 10
    sum = sum + last_digit
    product = product * last_digit
    count = count + 1
    num = num // 10
print(sum)
print(product)
print(count)