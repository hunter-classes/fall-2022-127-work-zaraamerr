#exercise 4 and 6 chapter 10

def avg(n):
    # calculate the sum of the items
    sum = 0
    for item in n:
        sum = sum + item

    # divide by the number of items
    average = sum / len(n)
    return average 

def sum_of_squares(n):
    sum = 0;
    for item in n:
        sum = sum + item*item
    return sum


grades = [90,95,100,90]
print("grades:",grades)
average=avg(grades)
print("Average:",average)

n = [3,4,5]
print("n:",n)
print("sum of squares:",sum_of_squares(n))