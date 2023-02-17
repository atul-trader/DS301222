# datatime module
# inbuild module
# helps to code wrt to date and time

import datetime as dt

current_date = dt.datetime.now()
print(current_date)

year = current_date.year
print("Year : ",year)

month = current_date.month
print("Month : ",month)

day = current_date.day
print("Day : ",day)

hr = current_date.hour
print("Hour : ",hr)

mins = current_date.minute
print("Minute : ",mins)

secs = current_date.second
print("Second : ",secs)

print("A : ",current_date.strftime("%A"))

print("a : ",current_date.strftime("%a"))

print("B : ",current_date.strftime("%B"))

print("b : ",current_date.strftime("%b"))

print("C : ",current_date.strftime("%C"))

print("c : ",current_date.strftime("%c"))

print("D : ",current_date.strftime("%D"))

print("d : ",current_date.strftime("%d"))

print("S : ",current_date.strftime("%S"))

print("X : ",current_date.strftime("%X"))

print("x : ",current_date.strftime("%x"))

d = dt.datetime.strptime("22:30", "%H:%M")
print(d.strftime("%I:%M %p"))

