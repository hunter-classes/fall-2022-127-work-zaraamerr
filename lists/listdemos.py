s= "this is a string"
elist=[]
l1=[1,2,3,4,5,6,7,8]
print (l1)
l2=["hello", "good morning", "ciao", "adios"]
print (l2)
l3=["hello", 3, 4, 5, "good night", 7, 9, 11]
print (l3)
l4=["one", 45, ['a', 'b', 'c'], "nice", [10,12,13]]
print (l4)
slice= l1[1:5]
print (slice)
longer_string= s+s
print (longer_string)
longer_list= l1+l4
print (longer_list)

#strings are inmutable 
# instead you can do this

new_string= s[:5]+ 'I' +s[6:]
print (new_string)

#we can also change lists directly
l4[4]: 99999
print(l4)

#you can change a list's elements
#but that isn't encouraged
#since you don't return anything
#which can be confusing to programmers

#this is slightly better
def change_in_place(l, index, new_value):
   l[index]= new_value
   return
print (l1)
change_in_place(l1, 4, 23)
print (l1)

print ("---------------------------------")

#this is an example of aliasing (aka shallow copy)
# it can be powerful but you have to be careful
# and make sure you're not changing any lists
# that you don't wanna change

l2=l1
print("l1:", l1)
print ("l2:", l2)
l1[4]=999
print ("l1:", l1)
print ("l2:", l2)

#this is how you would usually do
# a function to change part of a list
# when you want to follow the functional paradigm

def change_value(l, index, value):
  result=[]
  for item in l:
    #notice we can stick a variable
    #like item in [] to make it a list
    # then add it to a list to result which is also
    # a list so result = result + [item]
    # or we can call the list method and append item
    #result.append(item)
    #result= l.copy()
    result=l[:]
    result[index]=value
    return result

l2  = change_value(l1,4,1111)
print("l1:",l1)
print("l2:",l2)
    