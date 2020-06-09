#creating a set
languages = {"Python","ASP.net","C#","PHP"}
print(languages)

for item in languages:
    print(item)

# Operations on Set--Add,update,Remove,pop etc
languages.add("Android")
print(languages)

languages.update(["Go","Java"])
print(languages)

languages.update({'a':1,'b':2})
print(languages)

len(languages)

if "Go" in languages:
    #print("Element found in Set")
    languages.remove("Go")

print(languages)

languages.discard("a")
print(languages)

languages.remove("a")

languages.discard("a")

languages.clear()

languages

del languages

languages

#Set operations - Union
names1 = {"Pakistan","US","Australia"}
names2 = {"UK","UAE","US","China"}
names1.union(names2)

names1 | names2

x1 = {1,2,3}
x1 | ('4','5')

x1.union(('4','5'))

#Intersection--common elements in both sets
names1.intersection(names2)

print(names1.difference(names2))

print(names2.difference(names1))