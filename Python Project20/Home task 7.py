cash_leftovers = 0
coins = 0
cost = int(input())
if cost <= 0:
    print('Mage cant help you')
else:
    coins = cost // 25
    cash_leftovers = cost % 25
    if cash_leftovers > 0:
        coins = coins + cash_leftovers // 10
        cash_leftovers = cash_leftovers % 10
        if cash_leftovers > 0:
            coins = coins + cash_leftovers // 5
            cash_leftovers = cash_leftovers % 5
            if cash_leftovers > 0:
                coins = coins + cash_leftovers // 1
                cash_leftovers = cash_leftovers % 1
    print('You need to pay', coins, 'coin(s)')