import datetime
# def greet_with_time(func):
#     def wrapper(name):
#         current_time=str(datetime.datetime.now().time())
#         func(name+'!The time is currently'+current_time)
#     return wrapper
#
# @greet_with_time
# def greet(name):
#     print("Hello,"+ name)
# name=input("Enter your name::")
# greet(name)
print("______________________________________________________________")


# def authenticate(func):
#     def wrapper(name):
#         if name=="John":
#             func(name)
#         else:
#             print("Access denied")
#     return wrapper
#
# def greet_with_time(format_string):
#     def actual_decorator(func):
#         def wrapper(name):
#             current_time=datetime.datetime.now().time()
#             formatted_time=current_time.strftime(format_string)
#             func(name+ "!The time is currectly"+formatted_time)
#         return wrapper
#     return actual_decorator
# @authenticate
# @greet_with_time("%I:%M,%p")
# def greet(name):
#
#     print("Hello,"+name)
# greet("John")
# print("______________________________________________________________")

# def site():
#     print("Python Programming... im calling by the variable")
# website=site
# print(f"{site= }",)
# print(f"{website= }")
# # site()
# website()
# print("______________________________________________________________")
# def sqrt(num):
#     return num **0.05
# def square(num):
#     return num **2
#
# def math(function):
#     print(function(4))
#
# math(sqrt)
# math(square)
# print("______________________________________________________________")

# def math():
#     def square(num):
#         return num**2
#     print(square(2))
# math()
# print("______________________________________________________________")
# def math(num):
#     def square():
#         return num**2
#     print(square())
# math(2)
# print("______________________________________________________________")

# def sum_decorator(func):
#     def inner_deco():
#         print("The addition of two odd number 3 and 7")
#         func()
#         print("Is always an even number")
#     return inner_deco
#
# @sum_decorator
# def odd_add():
#     print(3+7)
# odd_add()
# print("______________________________________________________________")

###########Python args#############################
# def add(*num):
#     sum=0
#     for n in num:
#         sum=sum+n
#     print("Sum::",sum)
# add(2,6)
# add(3,4,5,6,7)
# add(1,2,3,4,5,6,7,8)
# print("______________________________________________________________")

# def Person(**kwargs):
#     for key,value in kwargs.items():
#         print("{}-{}".format(key,value))
# Person(Name='Prajwal',Gen='Male',Age=23,City='Shimogga',Mobile=6361303689)
#
# def func(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)
# func(1,3,10,20,Name='Kumar',salary=30000)
# print("______________________________________________________________")

def intro(**data):
    print("\nData type of argument:",type(data))
    for key,value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Prajwal",Lastname="kumar",Age=23,Phone=9742459123)
intro(Firstname="Manoj",Lastname="MP",Email='manoj@gmail.com',Country="London",Age=22,Phone=123456789)
