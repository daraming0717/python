num = int(input())

for _ in range(num) :
    array = list(map(int,input().split()))
    array.sort()
    print(array[-3])
