#question 1

import statistics
#1 Sort the list and find the min and max age

ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort()
print("minimum age and maximum age is: ",min(ages),max(ages))

#2 Add the min age and the max age again to the list
ages.extend([ages[0],ages[len(ages)-1]])
ages.sort()
print("after adding minimum age and maximum age: ",ages)

#3 Find the median age (one middle item or two middle items divided by two)
x=statistics.median(ages)
print("median is: ",x)

#4 Find the average age (sum of all items divided by their number)
print("average is: ", int(sum(ages)/int(len(ages))))

#5 Find the range of the ages (max minus min)
range=max(ages)-min(ages)
print("range is: ",range)
