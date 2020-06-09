#Creating a Dictionary
d = {}
print(d)
print(type(d))

mobile = {"brand":"Samsung",
         "model":"S10",
         "price":[550,560]}
mobile

mobile["brand"]

mobile.get("price")

# Operations on Dictionary

for x in mobile:
    print("{} has value {}".format(x,mobile[x]))

for x,y in mobile.items():
    print(x,y)

for x in mobile.values():
    print(x)

for x in mobile.keys():
    print(x)

# use in to Check if Key Exists
if "color" in mobile:
    print("Yes, it is one of the keys in mobile dictionary")
else:
     print("No, it is not listed in the keys of mobile dictionary")

len(mobile)

mobile['color'] = "White"

print(mobile)

mobile['model'] = 'S20'

print(mobile)

mobile.pop('price')
print(mobile)

mobile.popitem()

print(mobile)

new_dict = {}
new_dict = mobile.copy()
print(new_dict)

mobile.clear()

print(mobile)

del mobile

print(mobile)

#Taking user input in Dictionary

user_dict = {"Company":"",
            "Age":0,
            "NetWorth":""}
user_dict["Company"] = input("Enter company name: ")
user_dict["Age"] = input("Enter company Age: ")
user_dict["NetWorth"] = input("Enter company Net worth: ")

print(user_dict)