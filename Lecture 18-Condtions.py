late = False
if late:
    print("I will miss my flight")
print("_________________")
print("Ënd of If")

num = 5
if num>0 :
    print("number is positive")

#If---else Construct

num1 = 12
num2 = 5
if num1 > num2 :
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")

string = "Hello"
if "o" in string:
    print("o is present in string")
else:
    print("o is not found")

# example of If-ELSE  Sign-in
username = input("Enter username: ")
password = input("Enter password: ")
if username == 'admin@skillcurb.com' and password == "123":
    print("Logged in successfully! :)")
else:
    print("Incorrect username or password,try again")

salary = 5000
bonus = 0
designation = input("Enter designation")
if designation == "Clerk":
    bonus = 100
    salary = salary + bonus
elif designation == "Junior Developer":
    bonus = 1000
    salary = salary + bonus
elif designation == "Team Lead":
    bonus = 1500
    salary = salary + bonus
elif designation == "Manager":
    bonus= 2000
    salary = salary + bonus
print("You earned bonus", bonus)
print("Your salary for this month is", salary)

#nested if else

num = -3
if num>=0:
    if num==0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")