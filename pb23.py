x = int(input("enter x: "))
y = int(input("enter y: "))

cnt = 0

f_x = [0]*10
f_y = [0]*10


if x==0:
    f_x[0]=1
while x :
    f_x[x%10]=1
    x//=10
if y==0:
    f_y[0]=1
while y:
    f_y[y%10]=1
    y//=10
for i in range(10):
    if f_y[i] and f_x[i]:
            cnt+=1
print(cnt)
print("Digits: ", end="")
for i in range(10):
    if f_x[i] and f_y[i]:
        print(i , end=" ")
