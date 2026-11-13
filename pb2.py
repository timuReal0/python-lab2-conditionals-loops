year = int(input("Enter the year : "))
day = int(input("Enter the day : "))

month=1
for i in range(1 , 13):
    if i==2:
        if year%4 or (year%100==0 and year%400):
            if day>28:
                month+=1
                day-=28
            else:
                break
        else:
            if day>29:
                month+=1
                day-=29
            else:
                break
    elif i<=8:
        if i%2 or i==8:
            if day>31:
                month+=1
                day-=31
            else:
                break
        else:
            if day>30:
                month+=1
                day-=30
            else:
                break
    else:
        if i%2:
            if day>30:
                month+=1
                day-=30
            else:
                break
        else:
            if day>31:
                month+=1
                day-=31
            else:
                break

print(f"{day}.{month:02}.{year}")
