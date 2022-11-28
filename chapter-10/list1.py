# exercise 2 chapter 10

# create an empty list called my list
myList=[]
# append the first 3 items to the list
myList.append(76)
myList.append(92.3)
myList.append("hello")
# concatenate the last 3 items to the list
myList= myList + [True]
myList= myList + [4]
myList= myList + [76]

print (myList)

#exercise 3 chapter 10

#start w/ the list from exercise 2
myList= [76, 92.3, "hello", True, 4,76]

#append apple and 76
myList.append("apple")
myList.append(76)
#insert cat at position 3
myList.insert(3, "cat")
#insert 99 at the start of the list
myList.insert(0,99)
#find the index of hello
print(myList.index("hello"))
#count the number of 76s in list
print(myList.count(76))
#remove the first 76 from the list
myList.remove(76)
# remove true from the list using pop and index
myList.pop(myList.index(True))

print(myList)