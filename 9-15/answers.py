# question 7

def is_even(n):
  """
  n: an integer
  returns: true if n is even, false otherwise
  """
  if n % 2 == 0:
    return True
  else:
    return False

#test trials

result= is_even(10)
print("The result is",is_even(10))
result= is_even(5)
print("The result is",is_even(5))

#question 8

def is_odd(n):
  """
  n= an integer
  returns: true if n is odd, false otherwise
  """
  if is_even(n):
     return False
  else:
    return True

#test trials

result= is_odd(10)
print("The result is",is_odd(10))
result= is_odd(5)
print("The result is",is_odd(5))

#question 10 & 11

def is_rightangled(a, b, c):
  """
  c is longest
  """
  return a*a + b*b == c*c

def is_rightangled2(a,b,c):
  """
  any order for the sides
  """
  return is_rightangled(a,b,c) or is_rightangled(b,c,a) or is_rightangled(a,c,b)

#test trials

result= is_rightangled(3,4,5)
print("The result is", is_rightangled(3,4,5))
result=is_rightangled(5,4,3)
print("The result is", is_rightangled(5,4,3))

print("The result is", is_rightangled2(4,5,3))

# coding bat
  # hello_name
def hello_name(name):
  return "'Hello"+ name +"!'"
  
#test trials
print(hello_name('Zara'))
print(hello_name('Michael'))

# make_out_word
def make_out_word(out,word):
  return out[:2] + word + out[2:]

#test trials
print(make_out_word('<<>>', 'cheese'))
print(make_out_word('[[]]', 'coding'))

#first_two
def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]

#test trials
print(first_two('computer'))
print(first_two('autumn'))