#this recursive function to find  the factorial of an integer

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x * factorical(x-1))
# num=3
# print(" the factorical of",num "is")


# def is_palidrome(l,r,s):
#     if  l>=r:
#         return True
#     if s[l] !=s[r]:
#         return False
#     return is_palidrome(l+1,r-1,s)
#
# my_string=input("enter your string:")
# l=0
# r=len(my_string)-1
#
# check = is_palidrome(l,r,my_string)
#
# if check:
#     print(f"{my_string} is palidrome")
#
# else:
#     print(f"{my_string}is not palidrome")


#reverse
# def reverse_list(my_list,l,r):
#     if l>=r:
#         return my_list
#
#     tem =my_list
#     my_list[l]=my_list[r]
#     my_list[r]=tem
#
#     return reverse_list(my_list,l+1,r-1)
# my_l =[3,1,5,6,7]
# l=0
# r=len(my_l)-1
# print('my_list:',my_l)
# print('reverse_list :',reverse_list(my_l,l,r))
#
#
#
# def cal_sum(num):
#     if num == 1:
#         return 1
#     else:
#         return num+cal_sum(num-1)
# res=cal_sum(6)
# print(res)
#
# def cal_sum():
#     def cal_sum1():
#         num=int(input("enter any number ::"))
#         if num==1:
#             return 1
#         else:
#             return num+cal_sum1()
#     return cal_sum1()
# res=cal_sum()
# print(res)


