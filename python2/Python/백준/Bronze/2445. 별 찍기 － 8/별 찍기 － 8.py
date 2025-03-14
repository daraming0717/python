n = int(input())
for i in range(n-1, 0, -1) :
    print('*' * (n - i), end = '')
    print(' ' * (2 * i), end = '')
    print('*' * (n - i))
for i in range(0, n+1) :
    print('*' * (n - i), end = '')
    print(' ' * (2 * i), end = '')
    print('*' * (n - i))