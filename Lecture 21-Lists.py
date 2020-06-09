Veggies = ["Carrot","Potato","Turnip","Onion","Broccoli"]
print(Veggies)

Veggies[0]

Veggies[5]

Veggies[-1]

Veggies[:4]

Veggies[-2:-1]

#Operations on List----Iteration, Concatenation, Repitition, Insertion, Deletion etc

#Concatenation
Fruits = ["Apple","Cherry","Pineapple"]
NewList = Veggies + Fruits
print(NewList)

Veggies

Fruits

Veggies.extend(Fruits)

Veggies

L1 = [1,2,3,4,5]
L1 * 5

#Iteration
for x in Veggies:
    print("We have",x)

Veggies[0] = "Capsicum"
Veggies

Veggies.append("Beetroot")
print(Veggies)

len(Veggies)

#insertion
Veggies.insert(2,"Cabbage")
print(Veggies)

Veggies.remove("Apple")

print(Veggies)

del Veggies[1]
print(Veggies)

Veggies.pop()
print(Veggies)

mylist = []
print(mylist)

mylist = Veggies.copy()
print(mylist)

mylist.sort()

print(mylist)

max(mylist)

min(mylist)

max(L1)

min(L1)