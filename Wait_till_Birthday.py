import datetime as dt
import array
import re

no_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]

#List of Months in the year
Months = []
Months.append('January')
Months.append('February')
Months.append('March')
Months.append('April')
Months.append('May')
Months.append('June')
Months.append('July')
Months.append('August')
Months.append('September')
Months.append('October')
Months.append('November')
Months.append('December')

#Getting the date of birth
dob = input("What is your date of birth(dd/mm/yyyy): ")
dmy = re.split(pattern = r"[-_\|\.\+ ]", string=dob)
d = dmy[0]
m = dmy[1]
y = dmy[2]

#Getting the Current date
crdate = str(dt.date.today())
cudate = re.split(pattern = r"[-_\|\.\+ ]", string=crdate)
cud = cudate[2]
cum = cudate[1]
cuy = cudate[0]

bdyear = 0

#Checking if the entered no. of days is acceptable according to the no. of days in that month
if int(d) > no_of_days[int(m) - 1]:
    print("You can't Joke around here!!")
    exit(1)

#Checking if Leap Year and Changing the no. of days in February
ifleap = False
if(int(y) % 4 != 0):
    no_of_days[1] = 28
    ifleap = False
        
if(int(y) % 4 == 0):
    no_of_days[1] = 29
    ifleap = True
        
#No. of days between the start of the year and birthday
daysbod = 0
i = 0
while i< int(m)-1:
    daysbod += no_of_days[i]
    i += 1
daysbod += int(d)

#No. of days between the start of the year and current date
dayscu = 0
x = 0
while x< int(cum)-1:
    dayscu += no_of_days[x]
    x += 1
dayscu += int(cud)
#Total no. of days in the following year
total_days = 0
for n in no_of_days:
    total_days += n

dayspen = 0
daysleft = 0
if int(cum)<int(m):    
    for u in range(int(cum),int(m)+1):
        if u==int(cum):
            daysleft += (no_of_days[int(cum) - 1] - int(cud))    
        if u!=int(m) and u!= int(cum): 
            daysleft += no_of_days[u - 1]
        if u==int(m):
            daysleft += int(d)
elif int(m)<int(cum):
    for z in range(int(m), int(cum)+1):
        if z==int(m):
            dayspen += no_of_days[z - 1] - int(d)
        if z!=int(m) and z!=int(cum):
            dayspen += no_of_days[z - 1]
        if z==int(cum):
            dayspen += int(cud)
    daysleft = total_days - dayspen
elif int(m) == int(cum) and int(d)>int(cud):
    daysleft += int(d) - int(cud)
elif int(m) == int(cum) and int(d)<int(cud):
    daysleft += 360 - (int(cud) - int(d))

#Adding case to the date ie. st, nd, rd, th eg. 1st 3rd 26th ( This is what I call 'case' (-@_@-) )
def givecase(date: int):
    casedate = ""
    if date == 1:
        casedate = "1st"
    if date == 2:
        casedate = "2nd"
    if date == 3:
        casedate = "3rd"
    if date > 3: 
        casedate = str(date) + "th"  
    return casedate

#The Outputs
print("You were born on", givecase(int(d)), "of", Months[int(m)-1], "in", str(y), ". So.... (+-+)")
if daysleft != 0:print("There's",str(daysleft), "days left for your BirthDay. (^0^)")
if daysleft < 11 and daysleft != 0: print("Only", daysleft, "days left buddy! (^_^)")
if daysleft == 365 and ifleap: print("Can't wait for next birthday after celebrating it yesterday? (+_+)")
if daysleft == 364 and ifleap != True: print("Can't wait for next birthday after celebrating it yesterday? (?-?)")
if daysleft < 30 and daysleft != 0: print("Think about the presents already. (%~%)")
if daysleft == 0: print("You are just making fun of me!! (-_-)")
if daysleft == 1: print("~~~Just 1 long day~~~ (^_^)")
if daysleft < 183 and daysleft >100: print("After half year of wait. (,_,)")
if daysleft < 100 and daysleft < 11: print("A little Wait (#_#)")
if int(y) < 1950: print("And yeh.. are you a time traveller? ('-')")
if int(y) < 1500: print("Like someone from the Viking. (^_^)")
if int(y) < 1800: print("And yeh.. Your date of birth is probably not correct because the calender system has changed since your time. (*-*)")
if int(y) > int(cuy): print("You really are a time traveller")
if int(y) > int(cuy) - 5: print("First learn to read you kid. (@~@)")