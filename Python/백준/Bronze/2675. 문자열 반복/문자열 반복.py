t = int(input())
p=''
for _ in range(t) :
    r, s = input().split()
    r = int(r)
    for i in range(len(s)) :
        p += s[i] * r
    print(p)
    p=''