from datetime import datetime, date

year = int(input('Enter you birth year'))
month = int(input('Enter your birth month'))
day = int(input('Enter you birth day'))

date = datetime(year =  year, month =month, day = day)
now = date.today()


day_diff = now - date
month_diff = (now.year - year) * 12 + (now.month - month)
year_diff = now.year - year

print(f"DAYS = {day_diff} \nMONTH = {month_diff} \nYEARS = {year_diff}")

from datetime import datetime, date
year1 = int(input('Enter you birth year'))
month = int(input('Enter your birth month'))
day = int(input('Enter you birth day'))


now = date.today()
# date = datetime(year =  year1, month =month, day = day)
date1 = datetime(year =  now.year, month =month, day = day).date()
date2 = datetime(year = now.year+1, month = month, day = day).date()

if date1.month < now.month:
    days_till = date2 - now
else:
    days_till = date1 - now

print(days_till)

from datetime import datetime, date, timedelta

now = input('Enter todays datetime e.g year-month-day hour:time')
hours = int(input('Enter the duration of hours'))
minutes = int(input('Enter the duration of minutes'))

date1 = datetime.strptime(now, '%Y-%m-%d %H:%M')
date2 = timedelta(hours = hours, minutes = minutes) 
end_time = date1 + date2

print(f"The meeting will end  at {end_time}")

from datetime import datetime
import pytz

dt_str = input('Enter your date and time')
fro = input('Enter  your timezone')
to = input('Enter what country to convert into')

dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M' )

tz = pytz.timezone(fro)
localized_dt = tz.localize(dt)

target = pytz.timezone(to)
convert = localized_dt.astimezone(target)

print(convert)

import time
from datetime import datetime, date

t = input("Enter future date and time %Y-%m-%d %H:%M:%S : ")
d = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
now = datetime.now()
seconds = (d - now).total_seconds()
while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)  # wait 1 second
    seconds -= 1

print("Time's up")

import re

def validate_email(email):
    # Simple regex pattern for basic email validation
    pattern = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    )
    if pattern.match(email):
        return True
    else:
        return False

email = input("Enter an email address: ")

if validate_email(email):
    print("Valid email address!")
else:
    print("Invalid email address.")

def number(num):

    num1 = num[:3]
    num2 = num[3:6]
    num3 = num[6:8]
    num4 = num[8:10]
    phone_number = '(' + num1 + ') ' + num2 + '-' + num3 + '-' + num4
    # print(num1)
    # print(re.findall('[0-9]{3}[0-9]{2}', num))
    # print(re.findall(r"998\d\d", num))

    print(phone_number)

number('1234567998')

import re

def password(pswrd):
    if len(pswrd) <8:
        print('Your password is too short')
    
    elif re.search("[A-Z]", pswrd) is None:
        print('Your password should contain at leat 1 uppercase letter')
    elif re.search('[a-z]', pswrd) is None:
        print('Your password should contain at leat 1 lowercase letter')
    elif re.search(r'\d', pswrd) is None:
        print('Your password should contain at least 1 digit')
    else:
        return 'Password is created successfully'
    
password('Mohinur2402')

text = "Python is great. I love Python because Python is easy to learn."

word_to_find = input("Enter a word to find: ")
word_to_find = word_to_find.lower()
import string 
text = text.lower().translate(str.maketrans('','', string.punctuation)).split()

found_positions = []
for i, w in enumerate(text):
    print(w)
    if w == word_to_find:
        found_positions.append(i)

if found_positions:
    print(f"word {word_to_find} is found at positions {found_positions}")
else:
    print('No word is found')

def extract_numb(text):
    match = re.findall(r'\d', text)
    if match:
        print(''.join(match))
    else:
        print('No digits found')



extract_numb("s;aflj2402")
