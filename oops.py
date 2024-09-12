# class Student:
#     def Stud_info(self):
#         self.name=input("Enter name::")
#         self.age=int(input("Enter age::"))
#
#     def display(self):
#         print(self.name,self.age)
# S1=Student()
# S1.Stud_info()
# S1.display()


# class cars:
#     # def _init_(self,name,color,price):
#     #     .price=price
#     def cars_info(self):
#         self.name=input("enter name")
#         self.color=input("enter the color")
#         self.price=int(input("enter the price"))
#     def display(self):
#         print(self.name,self.color,self.price)
#
# c1=cars()
# c1.cars_info()
# c1.display()

# class Abc_comp:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def comp_info(self):
#         print("We are product based company")
# class Employee(Abc_comp):
#     def __init__(self,name,age,salary,address,email):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.address=address
#         self.email=email
#     def emp_dtls(self):
#         print(self.name,self.age,self.salary,self.address,self.email)
# emp=Employee('Prajwal',23,23000,'shimogga','prajwal@gmail.com')
# emp.comp_info()
# emp.emp_dtls()
#

# class Be_Partical:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def comp_info(self):
#         print("We teach all technical course")
# class Student(Be_Partical):
#     def __init__(self,name,age,course,address,email):
#         self.name = name
#         self.age = age
#         self.course = course
#         self.address=address
#         self.email=email
#     def student_dtls(self):
#         print(f"""
# name::{self.name}
# age::{self.age}
# course ::{self.course}
# address::{self.address}
# email::{self.email}
# """)
#         #print(self.name,self.age,self.course,self.address,self.email)
# s1=Student('Prajwal ',23,'Python full stack','basaveshwara nagar','prajwal@gmail.com')
# s1.comp_info()
# s1.student_dtls()

# import math
# class mathematics:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def hcf(self):
#         num1, num2 = self.num1, self.num2
#         while num2:
#             num1, num2 = num2, num1 % num2
#         return num1
# class algebra(mathematics):
#     def __init__ (self):
#        pass
#
#     def lcm(num1, num2):
#         hcf = (num1, num2)
#         lcm = (num1 * num2)
#         return lcm
# class hcf_lcm(algebra):
#     def algebra_info(self):
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         print(self.num1,self.num2)
# m1=mathematics(36,25)
# m1.hcf()
# m1.lcm()
# m1.hcf_lcm()
# m1.algebra_info()
#


# class mathematics:
#     def __init__(self):
#         pass
#
#     def math_info(self):
#         print("Mathematics is the study of numbers and how they are related to each other and to the real world!!")
#
#
# class algebra(mathematics):
#     def __init__(self):
#         pass
#
#     def alge_info(self):
#         print("""
#  Algebra is a branch of mathematics that uses mathematical statements to describe relationships between things that vary.""")
#
#
# class area_of_triangle(algebra):
#     def __init__(self, base, height):
#         self.base = float(base)
#         self.height = float(height)
#
#     def values(self):
#         area = 0.5 * self.base * self.height
#         print("Area of the triangle is", area)
#
#
#
# # Creating an instance of area_of_triangle
# val = area_of_triangle(3, 4)
#
# val.math_info()
# val.alge_info()
# print(val.values())


class vehicles:
    def vehicle_info(self):
        print("""vehicle are part of our life. basically have  many types of two wheelers and four wheelers..""")

class car(vehicles):
    def car_info(self):
        print("""\n 1.cars is vehicle having four wheel things which has full accessiores of 
         headlight 
         brakeing 
         acclerator
         gears
         diesel or petrol 
        2.which having different type of model
        3.which having different type seat capacity""")




