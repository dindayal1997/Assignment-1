# Python program to find sum of all
# elements in list using recursion
 
# creating a list
list1 = [10,5,4,3,2,1]
 
# creating sum_list function
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
  
# Driver code    
total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)