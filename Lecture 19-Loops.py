course = "Python"
for x in course:
    print(x)

num = 10
for i in range(num):
    print("{} Python".format(i))

for x in range(10,20):
    print(x)

for x in range(1,20):
    if x % 2 ==0:
        print(x)

#While loops

n = 1
while n < 11:
    print(n)
    n = n+1
print("End of while loop")

factorial = 1
num = 4
while num > 0:
    factorial = factorial * num
    num = num -1
    print(factorial)
print("Value of factorial is",fact)

#Nested for loop

for i in range(6):                #outer loop
    for j in range(i):            #inner loop
        print('*', end='')        #character to be printed
    print('')
else:
    print("End of loops")