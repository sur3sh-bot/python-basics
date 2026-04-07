import calendar #import calendar module to work with calendar related functions
year=int(input("enter the year: ")) 
month=int(input("enter the month: ")) #enter the month as a number (1-12)
print(calendar.month(year,month))