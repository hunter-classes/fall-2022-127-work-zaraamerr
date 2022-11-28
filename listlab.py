#Write a function to find the smallest value in a list find smallest in a list of items

def find_smallest(l):
    current_small = l[0]
    for item in l[1:]:
        if item < current_small:
            current_small = item
    return current_small
#test function
l=[8,6,-4]
result=find_smallest(l)
print ("This is the smallest number", result)

#Write a function that returns a new list that contains all the odd items in the original list

#empty lists
list=[]
new_list=[]
#get all odd nums
def odds (list):
  for num in list:
    if num % 2 !=0:
      new_list.append(num)
  return new_list
#test function
new_list= odds(list=[4,5,6,8,9])
print (new_list)
      

#Write a function that takes a string and returns a new string where all the words are capitalized.

string= ""
def capitalize_string (string):
  string=string.upper()
  return string
string= capitalize_string("computer")
print (string)
string= capitalize_string("coding")
print (string)

#Write a function that takes a string and returns a new string with every word that's longer than 5 characters turned into uppercase

string= ""
def capitalize_string_5 (string):
  if (len(string))>5:
    string=string.upper()
    return string
  elif (len(string))<5:
    return string
string= capitalize_string_5("computer")
print (string)
string= capitalize_string_5("code")
print (string)

#Write a function that takes a list of numbers and returns a new list with each item squared

def square_list(l):
    result = []
    for item in l:
        result.append(item*item)
    return result
# test function
l= [3,2,4]
result= square_list(l)
print (result)


#Write a function that takes two lists of numbers and returns a new list where each item is the corresponding value of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]

def combine_add(l1,l2):
    result = []
    if len(l1) < len(l2):
        shorter = len(l1)
    else:
        shorter = len(l2)
    for i in range(shorter):
        result.append( l1[i] + l2[i] )
    if len(l1) > shorter:
        result = result + l1[i:]
    else:
        result = result + l2[i:]
    return result

# test function
l1=[1,2,4,6]
l2=[33,44,55,6]
result= combine_add(l1,l2)
print(result)

#chapter 10 # 10, 11, 12

def count_word_length(s):
    count = 0
    for word in s.split():
        if len(word) == 5:
            count = count + 1
    return count
#test the function
result= count_word_length("chives, corn, hairs, coders")
print (result)

def sum(l):
    result = []
    i = 0
    while l[i] % 2 != 0:
        result.append(l[i])
        i=i+1
    return result
# test function
l=[3,5,4,7]
result= sum(l)
print (result)

def up_to_sam(l):
    result = []
    i = 0
    while l[i] != "sam":
        result.append(l[i])
        i=i+1
    return " ".join(result)
#test function
l= ["juice", "label", "thrice", "code","python", "sam", "lid","vacuum"]
result= up_to_sam(l)
print (result)