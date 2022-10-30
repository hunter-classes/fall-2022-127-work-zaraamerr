
def findLargest(l):
    current_large = l[0]
    for item in l[1:]:
        if item > current_large:
            current_large = item
    return current_large
#test function
l=[5,8,9,0,34,76]
result=findLargest(l)
print ("This is the largest number:", result)
  
def freq(l,v):
  #frequency=0
  #for item in l:
    #if item==v:
      #frequency= frequency+1
  #return frequency
  return len([x for x in l if x == v])

#test the function
l= [1,1,1,1,1,1,1,4,4,4,4,3,3,3,2,2,2,2,5,5,5,1,1,1,1,1,4,4,4,4]
result= freq(l,5)
print(result)

result= freq(l,1)
print(result)

#list comprehension!!
l= [3,4,4,4,4,5,5,5,5,5,7,7,7,18,18,18,3,3,3,3,1,1]
frequency=len([x for x in l if x==5])
print (frequency)

def mode(l):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently
    if multiple values appear the same # of times and are
    most frequent, return any of them.
    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
    mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
    both of those values appear 3 times which is the most
    """
    modeSoFar = l[0]
    freqSoFar = freq(l,modeSoFar)
    for item in l[1:]:
        if freq(l,item) > freqSoFar:
            modeSoFar = item
            freqSoFar = freq(l,item)
            
    return modeSoFar

l= [4,3,4,2,3,2,2,2,2,2,4,4,4,4,4,5,5,5,5,3,3]
result= mode(l)
print (result)