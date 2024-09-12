# class Bank_Loans:
#     def bank_info(self):
#         print("We give all types of loans......")
#
# class Home_loan(Bank_Loans):
#
#     def Hloan_amt(self):
#         print("Home loan amount details...")
#         H_amt=int(input("Enter the amount::"))
#         if H_amt<4000000 or H_amt>2000000:
#             rate_interest= H_amt * 0.50
#             print(rate_interest)
#         elif H_amt<2000000 or H_amt>1000000:
#             rate_interest= H_amt *0.25
#             print(rate_interest)
#
#
# class Vechical_loan(Home_loan):
#
#     def Vloan_amt(self):
#         print("Vechical loan amount details...")
#         V_amt = int(input("Enter the amount::"))
#         if V_amt < 2000000 or V_amt > 1000000:
#             rate_interest = V_amt * 0.50
#             print(rate_interest)
#         elif V_amt < 1000000 or V_amt > 500000:
#             rate_interest = V_amt * 0.25
#             print(rate_interest)
# class Education_loan(Vechical_loan):
#
#     def Eloan_amt(self):
#         print("Education loan amount details...")
#         E_amt = int(input("Enter the amount::"))
#         if E_amt < 2000000 or E_amt > 1000000:
#             rate_interest = E_amt * 0.50
#             print(rate_interest)
#         elif E_amt < 500000 or E_amt > 1000000:
#             rate_interest = E_amt * 0.25
#             print(rate_interest)
# HL=Education_loan()
# HL.bank_info()
# HL.Hloan_amt()
# HL.Vloan_amt()
# HL.Eloan_amt()

# class Bank_loans:
#     pass
#
# class Health_loan(Bank_loans):
#     def Heth_loan(self):
#         H_money = int(input("Enter the money: "))
#         if 2000000 < H_money <= 4500000:
#             return H_money * 0.50
#         elif 1000000 < H_money <= 2000000:
#             return H_money * 0.25
#         else:
#             return "Invalid amount for Health Loan"
#
# class Education_loan(Bank_loans):
#     def Edu_loan(self):
#         E_money = int(input("Enter the amount: "))
#         if 2000000 < E_money <= 4500000:
#             return E_money * 0.50
#         elif 1000000 < E_money <= 2000000:
#             return E_money * 0.25
#         else:
#             return "Invalid amount for Education Loan"
#
# class Vehicle_loan(Bank_loans):
#     def veh_loan(self):
#         v_money = int(input("Enter the amount: "))
#         if 2000000 < v_money <= 4500000:
#             return v_money * 0.50
#         elif 1000000 < v_money <= 2000000:
#             return v_money * 0.25
#         else:
#             return "Invalid amount for Vehicle Loan"
# # v1=Vehicle_loan()
# # print( v1.veh_loan())
# # E1=Education_loan()
# # print(E1.Edu_loan())
#
# # Usage example
# H1 = Health_loan()
# print(H1.Heth_loan())


#########################################################################################################################
# import math
#
#
# class Maths:
#     def math_info(self):
#         print("Mathematics is the study of numbers and how they are related to each other and to the real world.")
# class Algebra(Maths):
#     def heart_pattern(self):
#         for row in range(6):
#             for col in range(7):
#                 if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print()
#     def armstrong(self, number):
#         digits = str(number)
#         num_digits = len(digits)
#         sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
#         return sum_of_powers == number
#
# class Geometry(Maths):
#     def area_of_triangle(self, base, height):
#         return 0.5 * base * height
#
#     def area_of_rectangle(self, length, width):
#         return length * width
#




####################################################################################################################
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
import math


class Maths:
    def math_info(self):
        print("Mathematics is the study of numbers and how they are related to each other and to the real world.")
class Algebra(Maths):
    def pyramid_pattern(self):
        print("Pyramid pattern::")
        n=int(input("Enter number of row::"))
        for i in range(1, n, +1):
            for x in range(0,n, -i):
                print("*", end="")
            print(end = "\n")
    def armstrong(self):
        print("armstrong number::")
        num=int(input("Enter ant 3 digit number::"))
        sum=0
        temp=num
        while num>0:
            d= num % 10
            sum+= d * d * d
            num //=10
        if sum ==temp:
            print("It is an armstrong number::")
        else:
            print("its is not armstrong number::")
class Geometry(Maths):
    def geo_info(self):
        print("Is having multiple geometrical figure")
class shapes(Geometry):
    print("area of shapes")
    def area_of_triangle(self):
        print("Finding the area of triangle::")
        l=int(input("Enter the value of lenght::"))
        b=int(input("Enter the value of breath::"))
        tri_area=0.5*l*b
        print("The area is:: ",tri_area)

    def area_of_rectangle(self):
        print("Finding the area of rectangle::")
        l=int(input("Enter the value of lenght::"))
        b=int(input("Enter the value of breath::"))
        rect_area=l*b
        print("The area is:: ",rect_area)


class Arithmetic(Maths):
    def lst_factorial(self):
        lst=[1,2,3,4,5]
        lst_fact=[]
        for x in lst:
            fact = 1
            for i in range(1,x +1):
                fact*=i

        print("The factorial is::", fact)

    def equation(self):
        mass_kg= int(input("What is your mass in kilogram::"))
        mass_stone=mass_kg * 2.2 /14
        print("you weight",mass_stone,"stone.")


al = Algebra()
al.math_info()
al.pyramid_pattern()
al.armstrong()
print("*********************************************************************************")
sh = shapes()
sh.geo_info()
sh.area_of_triangle()
sh.area_of_rectangle()
print("*********************************************************************************")
arithmetic = Arithmetic()
arithmetic.lst_factorial()
arithmetic.equation()




