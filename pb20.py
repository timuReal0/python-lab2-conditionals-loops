x=int(input())

y=x
n=0
while y:
    y//=10
    n+=1

s=0
y=x
cnt=0
put=0
while y:
    cnt+=1
    if (n-cnt+1)%2:
        s+=(y%10)*(10**put)
        put+=1
    y//=10

print(s)