#Aab
word = (input().upper()) #AAB
array = list(set(word)) #[A, B]
count_ = [] #문자의 개수를 확인

for i in array : #i 는 A와 B가 된다.
    count_.append(word.count(i)) #count_ = [2, 1]

if count_.count(max(count_)) >= 2:
    print("?")
else :
    print(array[count_.index(max(count_))])