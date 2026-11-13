number = int(input())
cnt = 0
while number:
    if number%10>(number//10)%10:
        cnt+=1
    number=int(input())

print(cnt)