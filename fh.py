


#except handling
# print("Handling exception using try...except....else...finally")
# try:
#     numerator=50
#     denom=int(input("Enter the denominator:"))
#     quotient=(numerator/denom)
#     print(quotient,"Division performed successfully")
# except ZeroDivisionError:
#     print("Denominator as Zero is not allowed")
# except ValueError:
#     print("Only Integers should be entered")
# else:
#     print("The result of division operation is ",quotient)
# finally:
#     print("OVER AND OUT")


# prices={'Pen':10,'Pencil':5,'Notebook':25}
# item=input('Get price of:')
#
# try:
#     print(f'the price of {item} is {prices[item]}')
# except KeyError:
#     print(f'the price of {item} is not know')
# else:
#     print(f'there is no error in the statement')

# try:
#     fact=1
#     num=int(input("enter any number::"))
#     for x in range(1,num+1):
#         fact*=x#fact=fact*x
#     print(f"The factorial of {x} is ::",fact)
# except ValueError:
#     print("Input only numbers not the alphabets")
# else:
#     print("finally got the answer")
# finally:
#     print("The code got its answer")


# def square_data(numbers):
#     if not isinstance(numbers,(list,tuple or set)):
#         raise TypeError(f"list or tuple expected,got '{type(numbers).__name__}' ")
#     return [number**2 for number in numbers]
# print(square_data([1,2,3,4,5]))
# print(square_data({1,2,3,4,5}))

