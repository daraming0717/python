H, M = map(int,input().split())
if M < 45 :
    M += 60
    H -= 1
if H < 0 :
    H +=24
M -= 45
print(H, M)