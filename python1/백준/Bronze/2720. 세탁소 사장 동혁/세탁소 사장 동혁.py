num = int(input())
coins = [25, 10, 5, 1]

for j in range(num) :
    money = int(input( ))
    pass
    for i in coins :
        print(money // i, end = ' ')
        money = money % i
    print()