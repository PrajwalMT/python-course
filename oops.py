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

import math
class mathematics:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def operation(self):
        self.add=self.num1 + self.num2
        self.sub=self.num1 - self.num2
        self.mul=self.num1 * self.num2
class algebra(mathematics)
    def __init__ (self):
        print("mathematics is the arthamatic subject")
    def method(self,num1,num2):
        self.num1=num1
        self.num2=num2
class hcf_lcm(algebra):
    def algebra_info(self):
        print(self.num1,self.num2)
m1=mathematics(36,25)
m1.operation()
m1.method()
m1.algebra_info()



