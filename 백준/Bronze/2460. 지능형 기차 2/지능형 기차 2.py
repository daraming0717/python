people = 0
list = []
num = 10
for _ in range(num) :
    leave, ride = map(int,input().split())
    people += ride
    people -= leave
    list.append(people)
print(max(list))