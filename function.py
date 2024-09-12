# Argument with return value
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
#
v1=int(input("enter the number::"))
v2=int(input("enter the number::"))
# print("___________________________________________")
print("select(1) for addition")
print("select(2) for subtraction")
print("select(3) for division")
print("-------------------------------------")
choice=int(input("enter the choice::"))
if choice==1:
    print(f"{v1}+{v2} addition is :: ",add(v1,v2))
if choice==2:
    print(f"{v1}-{v2} subtraction is :: ", sub(v1, v2))
if choice==3:
    print(f"{v1}/{v2} division is :: ", div(v1, v2))

###################################################################################################################
#Argument and no return values

# def multiply(x,y):
#     print("value of x = ",x)
#     print("value of y = ",y)
#     c=x*y
#     print(c)
# multiply(y=2,x=4)
# ##############################################################
#Function with no argument,no return value

#function Defination
# def factorial_number():
#     factorial=1
#     num=int(input("enter a number to get its factorial::"))
#     for i in range(1,num+1):
#
#         factorial=factorial*i
#         print("the factorial is ",factorial)
# factorial_number()
################################################################################################
#No aruguments with retrun values
#Program that retruns sum of the lists of number
# my_list=[23,44,66,74,23]
#
# def add_list():
#     sum=0
#     for list_items in my_list:
#         sum=sum+list_items
#     return sum
#
# result=add_list()
# print("the sum is",result)

#palindrom
# def is_palindrome(num):
#     num = str(num)
#     rev = num[::-1]
#     num == rev:
# v1 =int(input("enter the v1::"))
# result = is_palindrome(v1)
# if result:
#     print(f"{v1} is a palindrome.")
# else:
#     print(f"{v1} is not a palindrome.")


# def pallin(num):
#     real=str(num)
#     rev=real[::-1]
#     if real==rev:
#         print("pallindrome")
#     else:
#         print("not a pallindrome")
# num=int(input("enter the number"))
# pallin(num)











