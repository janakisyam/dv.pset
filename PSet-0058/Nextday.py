day = int(input("Enter Day: "))
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

month_day = 30

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 11):
    month_day=31
elif (month == 2):
    month_day=28
elif (year % 4 == 0 or year % 100==0 and year % 400 !=0 and month ==2):
    month_day=29

if (day >= month_day):
    month+=1
    day=1
elif (day < month_day):
    day+=1
if (month==12 and day==30):
    month=1
    day=1
    year+=1

print(day,month,year)
