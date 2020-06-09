#Lecture 25: Importing Data from CSV

#importing csv module
import csv

#reading from a csv file
with open('sample.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)

#writing to a csv file
myData = [["fname", "lname", "Country"],
          ['Smith', 'Brian', 'USA'],
          ['Tom', 'Alex', 'UK']]
with open('myfile2.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=';',lineterminator='\n')
    csv_writer.writerows(myData)
print("File has been written successfully")