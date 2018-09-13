'''- 1 Jan 1900 was a Monday.
- Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.'''

#year = 1901
#month = 1
day=0
d=1
#day = ["M","T","F".""]
#month = 1
sunday = 0
for year in range(1901,2001):
    for month in range(1,13): #to check month
        days_month=30
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12 or month==10):
            days_month=31
        elif (month == 4 or month == 6 or month == 11 or month==9):
            days_month=30
        elif (month == 2):
            days_month=28
        elif (year % 4 == 0 or year % 100==0 and year % 400 !=0 and month ==2):
            days_month=29
        for days in range(1,days_month+1):
            d+=1
            day+=1
            if(d%7==0 and day==1):
                sunday+=1
                d=0
                #print(day)
            if(day==days_month):
                month+=1
            if(month==12 and day==31):
                year+=1
        day=0
print(sunday)
#READTHEQUESTIONWRONGAGAIN
'''for year in range(1901,2002):
    for month in range(1,13): #to check month
        days_month=30
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 12 or month==10):
            days_month=31
        elif (month == 4 or month == 6 or month == 11 or month==9):
            days_month=30
        elif (month == 2):
            days_month=28
        elif (year % 4 == 0 or year % 100==0 and year % 400 !=0 and month ==2):
            days_month=29
            d=0
        for days in range(1,days_month+1):
            d+=1
            day+=1
            if(d%7==0 and month ==1):
                sunday+=1
                print(sunday)
                print(day)
                #print(month)
                print(year)
                print("\n")
            if(day==days_month):
                month+=1
                #day=0
            if(month==12 and day==30):
                year+=1
        day=0
print(sunday)'''

#MISREADTHEQUESTION:
'''for year in range(1901,2001):
    for month in range(1,13):
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 11):
            days_month=31
        elif (month == 2):
            days_month=28
        elif (year % 4 == 0 or year % 100==0 and year % 400 !=0 and month ==2):
            days_month=29
        for d in range(1,8):
            d+=1
            day+=1
            if day == days_month:
                month+=1
                day=1
            if (d%7==0):
                sunday+=1
                d = 1
    if(month == 12 and days_month==31):
        year+=1
print(sunday)'''

'''for year in range(1901,2001):
    for month in range(1,13):
        d+=1
        day+=1
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 11):
            days_month=31
        elif (month == 2):
            days_month=28
        elif (year % 4 == 0 or year % 100==0 and year % 400 !=0 and month ==2):
            days_month=29
        if day == days_month:
            month+=1
            day=1
        if (month==1 and d%7==0):
            sunday+=1
            d = 1
        if(month == 12 and days_month==31):
            year+=1
print(sunday)'''
