import random
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
    freqSoFar = l.count(modeSoFar)
    for item in l[1:]:
        if l.count(item) > freqSoFar:
            modeSoFar = item
            freqSoFar = l.count(item)
            
    return modeSoFar

l= [4,3,4,2,3,2,2,2,2,2,4,4,4,4,4,5,5,5,5,3,3]
result= mode(l)
print (result)

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 

def testMode(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = mode(dataset)
    print("Mode: ",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)

testFindLargest(8000,30)
testMode(40000,30)

def fastMode(dataset):
    # find largest value in dataset
    largest=findLargest(dataset)
    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
    tallies=[0 for x in range (largest + 1)]
    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list
    for item in dataset:
      tallies[item]= tallies[item] + 1
    # 3. the index with the highest
    # value in tallies is the mode
    # find the bucket that has the largest value
    # that's the one that occurred the most
    mode_count=findLargest(tallies)
    return tallies
    # find and return the index that holds 
    #mode_count in tallies
    for i in range(len(tallies)):
      if tallies[i]==mode_count:
        return i

def testFastMode(size, maxvalue):
  dataset=buildRandomList(size,maxvalue)
  print(dataset)
  result= fastMode(dataset)
  print (result)

testFastMode(45,7)