# range should be from 1-100 with i inclusive
# if the number is divisible by 3, print 'fizz'
# if the number is divisible by 5, print 'buzz'
# if divisible by both 3 and 5, print 'fizzbuzz'
# if not divisible by 3 nor 5, print i

for i in range (1,101):
  if i % 3 == 0 and i % 5 == 0:
    print ("Fizzbuzz")
  elif i % 3 == 0:
    print ("Fuzz")
  elif i % 5 == 0:
    print ("Buzz")
  else:
    print (str(i))