n = int(input("Enter a number : "))

if n==0:
    print(f"The control digit of {n} is equal to 0")
elif n%9==0:
    print(f"The control digit of {n} is equal to 9")
else:
    print(f"The control digit of {n} is equal to { n%9 }")
