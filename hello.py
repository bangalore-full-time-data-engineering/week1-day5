In your README.md answer the following questions with True or False.

(5)==(5,) returns True False
Any of the following: (integer, string, list) can be the key of a dictionary. False
Any of the following: (integer, string, list) can be the value of a dictionary. True
Any of the following: (integer, string, list) can be in a set. True
s[0]="a" would result in an error if s is a string. True
If a = [(1,2),(3,4)] performing a[0]=3 would result in an error. False
If a key k is not in a dictionary d, then d[k] will return None. false
If ((x==y)!=(x is y)) is False, then x is an alias of y. False
If you were to open and read (so in \r" mode) a file that does not exist, Python will error out.True

 In your README.md answer the following questions:

What are logical errors and how are they different from syntax errors?

Is Python a compiled or scripting language? Explain the difference between the two.

What is the outcome of the following conditional statements if the value of variable x is 5? Show your work.

a. x <= 4 or (x != 9 and x > 10) false

b. x > 0 and x < 10 and x != 6 true

c. x == 1 or x > 0 True
   
import datetime

def double_day(bd1, bd2):
    person1 = datetime.datetime.strptime(bd1,'%Y/%m/%d')
    person2 = datetime.datetime.strptime(bd2,'%Y/%m/%d')
    today = datetime.datetime.today()
    age1 = today - person1
    age2 = today - person2
    double_day = age2 - 2*age1
    double_day = datetime.datetime.today() + double_day
    print("double day :" + str(double_day))
double_day("1980/10/10","1982/10/20")

import datetime
def n_time_age(bd1, bd2, n):
    bday1 = datetime.datetime.strptime(bd1,'%Y/%m/%d')
    bday2 = datetime.datetime.strptime(bd2,'%Y/%m/%d')
    tday = datetime.datetime.today()
    age1 = tday - bday1
    age2 = tday - bday2
    n_time_age = age2 - n*age1
    n_time_age = datetime.datetime.today() + n_time_age
    print(n_time_age)
         
n_time_age("1980/10/10","1982/10/20",10)
--------------------------------------------------------
cd documents
git clone
cd week1-day5
git checkout -b %branch_name% #branch name is the git user name 
# complete an exercise 
git add file name
git commit -m "%commit_message%"
git push origin %branch_name%
username
password

