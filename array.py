import array as arr
# number = arr.array('i',[10,20,30,40,50])
# print(number)
# print("-----------------------------------------------")
# for x in number:
#     print(x)
# print('--------------------------------------------------')
# a=arr.array('d',[1.1,2.1,3.1])
# print(a[1])
# print("----------------------------------------------------")
# a=arr.array('d',[1.1,2.1,3.1])
# print(len(a))
# print("===========================================================")
# a=arr.array('d',[1.1,2.1,3.1])
# a.append(3.4)
# print(a)
# print("===========================================================")
# a=arr.array('d',[1.1,2.1,3.1])
# a.extend([4.5,6.3,6.8])
# print(a)

# ##to add a d specific elelment at a particular index postion in the array,the insert (i,x) function can be used.
# a=arr.array('d',[1.1,2.1,3.1])
# a.insert(1,3.8)
# print(a)

# a=arr.array('d',[1.1,2.1,3.1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# c=arr.array('d')
# c=a+b
# print("Array c=",c)
# #print(c)
# print("===========================================================")

#WAP to find sum of all array elements
# sum=0
# number= arr.array('i',[1,2,3,4,5])
# for x in number:
#     # print(x)
#     sum+=x
# print(sum)
# # #WAP to reverse the array elements
# number=arr.array('i',[1,2,3,4,5])
# print(number[::-1])
#WAP to display the even number of an array and find their sum
# sum=0
# number=arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# for x in number:
#     if x%2==0:
#         print(x)
#         sum+=x
# print(sum)
#WAP to apply the slicing for an array
# number= arr.array('i',[1,2,3,4,5,6,7,8])
# print(number[2:1])
# print(number[:-5])
# print(number[:4])
#WAP to find the max and min number of an array
# number= arr.array('i',[1,2,3,4,5,6,7,8])
# print(max(number))
# print(min(number))
#WAP to delete particular element in an array
# number = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
# del(number[3])
# print(number)
# del(number[6])
# print(number)

#WAP to print the square and cube of an array
#for square
# a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
# for x in a:
#
#     x = x * x
#     print(x)
# print("=============================================================")
# #for cube
# a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
# for x in a:
#
#     x = x * x * x
#     print(x)
#WAP to display biggest and smallest number
# num_array=arr.array('i',[3,5,7,8,-1,4,10,12])
# if len(num_array)==0:
#     print("the array is empty")
# else:
#     max_num=num_array[0]
#     min_num=num_array[0]
# for num in num_array:
#     if num > max_num:
#         max_num = num
#     if num <min_num:
#         min_num=num
#     print(f"the maxinum number is {max_num}")
#     print(f"the mininum  number is{min_num}")
#
#multidimentional array
# arr1=[[0]*3]

# T=[[11,12,5,2],[15,6,10,5,],[10,8,12,5],[12,15,8,6]]
# print(T)
# print("_---------------------------------------------")
# for r in T:
#     for c in r:
#         print(c,end=" ")
#     print()
# print("=====================================================")
# T=[[11,12,5,2],[15,6,10,5,],[10,8,12,5],[12,15,8,6]]
# T.insert(2,[0,5,11])
# for i in T:
#     for c in i:
#         print(c,end=" ")
#     print()
# print("============================================================")
#
# #Matrix Using jion() function
# #the jion () method is a string method and returns a string in which the elements of the sequence have been jioning by the str searatcor
#
# m=[[1,2,3],[7,1,5],[0,9,3]]
# for i in m:
#     print("".join(str(i)))
# print("======================================================")
import array as arr
from numpy import reshape,array,ones,zeros,eye,arange
#
# a=ones((3,4),int)
# print(a)
# print("-------------------------------------------")
# b=zeros((3,4),int)
# print(b)
# print("_------------------------------------------------")
# c=eye(3)
# print(c)
# print("_------------------------------------------------")
# c=eye(2)
# print(c)
# print("_------------------------------------------------")

###############reshaping

# a=[1,2,3,4,5,6]
# b=reshape(a,(2,3))
# print(b)
# print("====================")
# b=reshape(a,(3,2))
# print(b)
# print("_------------------------------------------------")

#arrange
#lets tke a 1d array "a" with 12 elements as:

# a =arange(12)
# print(a)
# print("_------------------------------------------------")
# b=reshape(a,(2,3,2))
# print(b)
# print("_------------------------------------------------")
# b=reshape(a,(3,2,2))
# print(b)
# print("_------------------------------------------------")

# T=[[11,12,5,2],[15,6,10,5,],[10,8,12,5],[12,15,8,6]]
# m=[[1,2,3],[7,1,5],[0,9,3]]
# for i in T:
#     for c in m:
#         print(T,m)
#
#     print()
# a=[1,2,3,4,5,6],[7,8,9],[10,11,12]
# b=reshape(a,(2,3))
# print(b)

# a = arange(9).reshape(3,3)
# print(a)
# b = arange(9).reshape(3,3)
# b_t = b.T
# print(b_t)
#
# print(a+b_t)

# c=reshape(a,(4,3))
# print(c)
# sum= b+c
# print(sum)
# # sum=+b
# # print(sum)


import numpy as np

# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a[1:3,1:3])
# print(a[:,2:4])
# print(a[:,1])
# print(a[1,:])
# a=np.array([20,30,40,50])
# print(a)
# print("++++++++++++++++++++++++++++++++++++")
# b=np.arange(4)
# print(a+b)
# print("========================================")
# print(np.add(a,b))
# print("----------------------------------------")
# print(a-b)
# print(np.subtract(a,b))
# print("__________________________________________")
#
#
# A=np.array([[1,1],[6,1]])
# B=np.array([[2,8],[3,4]])
# print(A*B)
# print(np.multiply(A,B))
# print("______________________________________________")
# print(np.divide(A,B))
# print(A/B)

# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# print(my_data)
# print(22 in my_data)
# print(2 in my_data)
# print(88 not in my_data)
# print(101 not in my_data)

# tpl = (2, 4, 5, 7, 8, (10,17,23),45,23)
# print(tpl[:])
# print(tpl[:3])
# print(tpl[4:])
# print(tpl[-3:])
# print(tpl[2:5])


# Negative Index:
# my_tuple = 3, 4.6, "dog"
# print(my_tuple)


