def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    result = ""
# isolate, uppercase and add first init to result
    first = name[0]
    first = first.upper() 
    result = result + first + "."

# find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result

# test Initialize
result= initialize("james bond")
print("james bond -->", result)

def bondify(name):
    """
    input: a string in the form "first last"
    return:string in the form "Last, First Last"
    """
    result=""
# find the place where the first and last name are separated by a space
    location= name.find(' ')
   #establish and capitalize the first name
    first= name[0:location]
    first= first.capitalize()
   #establish and capitalize the last name
    last= name[location+1:].capitalize()
#add first and last name to the result in the form last, first, last
    result= last + "," + " "+ first + " " + last
    return result

#test bondify
result= bondify("james bond")
print ("james bond -->", result)

def piglatin(word):
  """
  input: a string representing a word
  returns: a new string w/ the word in piglatin

  Rules:
  if the first letter is a consonant, move it 
  from the start to the end and add "ay" so
  "hello" becomes "ellohay"

  If the first letter is a vowel, just add "yay"
  to the end.

  try to handle uppercase words
  """

  if word[-1] in ".!?":
        end_of_sent = True
        punctuation = word[-1]
        word = word[:-1]
  else:
        end_of_sent = False

    # keep track of if the word had a capital letter
  if word[0] == word[0].upper():
        capital = True
  else:
        capital = False
    
    # transform to lower case
  word = word[0].lower()+word[1:]
  first = word[0]

    # turn into piglatin
  if first in 'aeiou':
        result = word + 'ay'
  else:
        result = word[1:]+first+'ay'
    
    # if we started with a capital letter we
    # have to transform the result back to have
    # a capital letter
  if capital:
        result = result.capitalize()
    
    # test to see if we have to add punctuation on at the end
  if end_of_sent:
        result = result + punctuation
  return result

result = piglatin("cheese")
print ("cheese -->", result)
result = piglatin ("Cheese!")
print ("Cheese! -->", result)