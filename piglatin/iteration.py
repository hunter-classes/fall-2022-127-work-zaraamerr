import random
#foreach loop
for counter in range (5):
  print (counter)

for letter in "this is a sentence":
  print(letter)

# while loop
  loop_counter=0
while random.randrange (0,100) < 80:
  print ("hello", loop_counter)
  loop_counter= loop_counter +1

print ("This above loop ran this many times:", loop_counter)

#while loop is a counting loop
#first set up a variable to hold the count
t= 0
# then use the boolean to indicate when to stop
while t < 5:
  print (t)
  t=t+1 

while t > 0:
  print (t)
  t= t-1

#you can also traverse over a string

s= "hello world"
t=0

while t < len(s):
  print(s[t])
  t= t+1
  