import csv
#flawed split example
#f= open ('demo.csv')
#for line in f.readlines():
  #print (line)
  #line= line.strip()
  #print(line.split(","))

#example using csv module into a list
reader=csv.reader(open("demo.csv"))
for line in reader:
  print(line)