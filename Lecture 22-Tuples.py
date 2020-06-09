#creating a Tuple
tpl1 = (1,2,3,4,5)
tpl2 = 10,20,30
print(tpl1)
print(tpl2)

type(tpl1)

type(tpl2)

tpl3 = ("cat",12,True,36.56)
tpl3

t1 =("a",)
t1

type(t1)

tpl1[2]

tpl1[-1]

tpl1[2:5]

del tpl1

print(tpl1)

#Tuple Operations---Iteration, Concatenation, Repetition

colors = ("Red","Yellow","Green","Black")
colors

for x in colors:
    print(x)

#repetition
colors * 3

colors

user = input("enter the name of color: ")
if user in colors:
    print("{} is found in Colors".format(user))
else:
    print("{} is not found in Colors".format(user))

print(len(colors))

colors[0] = "White"
print(colors)

colors2 = ("White","Cyan","Aqua")
colors + colors2

#count
tpl = (1,2,3,2,57,8,8,9)
x = tpl.count(2)
print(x)

#index
tpl.index(2)

#unpack
tpl_new = ("cat","dog","fish")
x,y,z=tpl_new
print(x)
print(y)
print(z)