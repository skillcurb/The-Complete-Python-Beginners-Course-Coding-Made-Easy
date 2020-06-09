try:
    a = 5
    b = "variable"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')

try:  
    
    x = 5 / 0
except ZeroDivisionError as e:  
    # `e` is the exception object 
    print("Exception block: Got a divide by zero! The exception was:", e) 
    # handle exceptional case   
finally:
    print("finally Block: The END")

#nameError
name = 'SkillCurb'
try:
    print (name)
except NameError:  
    print ("NameError: name 'ans' is not defined")
else:
    print("Else block")

try:
    nb = int(input('Enter a number: ')) 
except ValueError:    
    print('This is not a number')

x = 10
if x > 9:
    
    raise Exception('x should not exceed 9. The value of x was: {}'.format(x))

try: 
    data = {1: 'one', 2: 'two'}
    print(data[3])
except KeyError as e:   
    print('key not found',e) 

try:
    with open('file.txt') as file:
        read_data = file.read()
        print(read_data)
except FileNotFoundError as fnf_error:
    print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')