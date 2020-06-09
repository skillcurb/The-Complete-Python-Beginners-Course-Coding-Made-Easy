topic = 'python is fun to learn'
print(topic)

print(topic.upper())

print(topic.lower())

print(topic.capitalize())

print(topic)

print(topic.islower())

print(topic.isupper())

#isalnum
address = '50NorthGarfieldlane'
print(address.isalnum())

print(address.isalpha())

address_zip = '11447'
address_zip.isnumeric()

address_zip.isdigit()

#difference between isdigit() and isnumeric()

str3 = u"½¼"        #fractional value
print(str3.isnumeric())
print(str3.isdigit())

#length of a string len
color = 'Red'
len(color)

str1 = "Welcome friends to Skill Curb"
print(str1.replace("friends","learners"))


print(str1)

# join()

s3 = "Hi, John. How are you doing?"
result_str = ' '.join(s3)
print(result_str) 

#split
s4 = s3.split()
print(s4)

#count-- count all occurences of a word

text2 = "I love Spring, Spring is my favorite season of the year."
occurence = text2.count("Spring")
print(occurence)

text2.find('S')

text2.find('S',13,-1)

text2.index('S')

text2.index('Z')

text2.find('Z')

fruit = "     Mango is my favorite fruit     "
z = fruit.strip()
print( z)

x=z.strip("Man")
print(x)

