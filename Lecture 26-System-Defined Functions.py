#zip() -- 
std_name = [ "Sarah", "Maria", "Smith", "Clark" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 90, 80, 60, 70 ]
mapped = zip(std_name,roll_no,marks)

mapped

type(mapped)

record = list(mapped)
print(record)

# sum()-- calculates sum of iterator
total_marks = sum(marks)
print(total_marks)

print(sorted(marks))

#map
names = ['Isadora','Bob','April']
names_length = map(len,names)
names_length

print(list(names_length))

# use dict()
mylist = [('a', 15), ('b', -25)]
mydict = dict(mylist)
print(mydict)

#consider a list of words and convert it into tuple
new_lst = ['sat', 'hat', 'fat', 'rat']
mytpl = tuple(new_lst)
print(mytpl)

set(mytpl)

#dir shows valid attributes of object
print(dir(mydict))

help(print)

operand = 11
print(eval('operand + 1'))

companies = ["IBM", "Google", "Apple", "Cisco"]
marks = [10,20,30,100]
print(max(companies))
print(max(marks))

print(min(companies))
print(min(marks))

#The chr() method takes a single parameter, an integer i.

#The valid range of the integer is from 0 through 1,114,111.
print(chr(97))

val = 9
print(id(val))

#slice
companies = ["IBM", "Google", "Apple", "Cisco"]

slice_val = slice(1,4,2)
print(companies[slice_val])
