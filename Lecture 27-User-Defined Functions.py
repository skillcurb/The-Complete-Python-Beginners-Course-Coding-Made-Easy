# function definition

def my_function():
    print("Hello from a function")

my_function() # function call

def modified_function(data):
    print("Hello "+data)

modified_function("Sarah")

data = input('Enter a name: ')
modified_function(data)

#this is incorrect and throw an error,as your function definition requires only one input paramter
modified_function('George','Emily')

# function definition with default argument
def my_function2(country = "Norway"):
    print("I am from " + country)
my_function2('USA')

my_function2()

# Keyword Arguments
def my_function(child1, child2):
    print("The youngest child is " + child2)

my_function(child1 = "Ivy", child2 = "Arthur")

# function with reference
def myfunction(x):
    x.append("20")
    return x

a = ["10"]
print ("value of argument a before calling function",a)

b = myfunction(a)
b

a #now values are also added in a 

def square(x):
    return (x*x)
print("The square of the number is : ", square(3))

print("The square of the x is {0}".format( square(3)))

# returning multiple values
def func(x):
    return x**2,x**3

num=int(input('Enter a number to calculate its square and cube: '))
a,b = func(num)
print('Square of {} is {}'.format(num,a))
print('Cube of {} is {}'.format(num,b))


# function to guess the lucky number
def luckyNum(): 
    lucky_num = 10
    number = 0
    while(number != lucky_num):
        number = int(input('Enter a number: '))
        if number == lucky_num:
            print('You guessed it correctly')
        else:
             print('Sorry incorrect, try again')
         
    
# Calling function 
luckyNum()