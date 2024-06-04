i = 9
array = []
for _ in range(i) :
    n = int(input())
    array.append(n)
print(max(array))
n = max(array)
print(array.index(n)+1)