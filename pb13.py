x = int(input("Enter a number : "))

n = 0
y=x
while y :
    y//=10
    n+=1
y=x
s=0
while y:
    s+=((y%10)**n)
    y//=10

if x==s:
    print("True")
else:
    print("No")