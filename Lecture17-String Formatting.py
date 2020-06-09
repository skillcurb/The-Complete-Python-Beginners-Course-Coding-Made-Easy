age = 23
sentence = "I am Sarah and I am "+age+"years old"
print(sentence)

age = 23
sentence = "I am Sarah and I am {} years old"
print(sentence.format(age))

str1 = "I have {} books and {} pens"
print(str1.format(3,2))

qty = 3
item = 'Doughnuts'
price = 3.95
sent ="I have bought {} {} which costs dollars"
print(sent.format(qty,item,price))

qty = 3
item = 'Doughnuts'
price = 3.95
sent ="I have bought {0} {1} which costs {2} dollars"
print(sent.format(qty,item,price))

print("{0} love {1}!".format("I", "Python"))
print("{1} is about {0}!!".format("String Formatting", "Lecture 17"))
print("{2} is the most widely {3} {1} {0}".format("language","programming", "Python", "used"))

sent = "Saarah has {s1} books,{s2} pencils and {s3} eraser".format(s1=3,s2=2,s3=1)
print(sent)

print("{st} is a great {1} for {0}".format("beginners", "choice",st ="Python"))

print("{st:>10} is a great {1} for {0}".format("beginners", "choice",st ="Python"))

print("{0:d}".format(12))

print("{0:05d}".format(12))

print("{:f}".format(3.14157))

print("{:8.3f}".format(3.14157))

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

print("{:+f} {:+f}".format(14.25, -14.23))

print("{:-f} {:-f}".format(14.25, -14.23))

print("{: f} {: f}".format(14.25, -14.23))

print("The binary version of 5 is {0:b}".format(5))

txt = "You scored {:.0%}"
print(txt.format(0.25))