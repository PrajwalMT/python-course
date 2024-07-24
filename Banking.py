# print("WELCOME TO ONLINE BANKING ")
# print(input("Enter your Account ID::"))
# print(input("Enter your Password::"))
# print("!! WELCOME  TO SBI !!")
# print("""
# 1.withdraw money
# 2.deposit money
# 3.log out
# """)
# a=10000
# user_choice= int(input("Enter your choice::"))
# if user_choice==1:
#
#     def withdraw (a,b):
#         return a-b
#     def deposit(a,b):
#         return a+b
# b= int(input("enter the amount of money you want withdraw::"))
# print("select(1) for withdraw")
# # print("select(2) for deposit")
# choice = int(input("enter the choice::"))
# if choice == 1:
#     print(f"{a}-{b} withdraw is :: ", withdraw(a,b))
# c= int(input("enter the amount of money you want deposit::"))
# if choice == 2:
#     print(f"{a}+{b} deposit is :: ", deposit(a,b))
#     print("Your bank balance amount is 200000")
# elif user_choice==2:
#     print("Enter the amount of money you want to withdraw::")

# Total_amount = 10000
# name=input("Enter the name:")
# password=input("enter the password:")
# print("welcome to SBI bank !")
#
#
# def withdraw(money,Total_amount):
#     Total_amount -= money
#     print(f"Your Bank Balance is {Total_amount}")
# def deposit(money,Total_amount):
#    Total_amount+=money
#    print(f"Your Bank Balance is {Total_amount}")
# def logout():
#      print("Thank you")
#      print("visit again")
#
#
# choice = [withdraw, deposit, logout]
# for i in choice:
#     choices = """
#     1)withdraw
#     2)deposit
#     3)logout
#     """
#     print(choices)
#     user_choice=int(input("enter the choice:"))
#     if user_choice == 1:
#         money = int(input("enter the money to withdraw"))
#         withdraw(money, Total_amount)
#
#     if user_choice == 2:
#         money = int(input("enter the money to deposit"))
#         deposit(money, Total_amount)
#
#     if user_choice == 3:
#         print("Thank you!!")
#     break


ids = ['Anitha', 'Namitha']
psw = ['12345', 'yo']
bal = [2000000, 70000]

idx_id = 0


# login
def acc():
    print('')

    accid = input('Enter your account id : ')
    print('')

    if (accid in ids):
        idx_id = (ids.index(accid))

        password = input('Enter your password : ')
        if (password in psw and password == psw[idx_id]):

            print('')
            print('Welcome!!')

            activity(idx_id)
        else:
            print('wrong password')
            acc()
    else:
        print('wrong id......')

        print('')

        print('This id does not exist! ')
        create_acc()


# activities to do
def activity(idx_id):
    print('')
    print('Your bank balance amount =', bal[idx_id])

    opt = int(input('Do you want to withdraw money (1)/deposit money (2)/log out (3) : '))

    while (opt != 3):

        if (opt == 1):

            print('')

            x = int(input('Enter the amount of money you want to withdraw : '))
            total = bal[idx_id] - x

            bal[idx_id] = total

            print('')

            print('You have recieved rupees', x)

            print('')

            print('1.Your bank balance amount =', bal[idx_id])




        elif (opt == 2):

            print('')

            x = int(input('Enter the amount of money you want to deposit : '))
            total = bal[idx_id] + x

            bal[idx_id] = total

            print('')

            print('You have deposited rupees', x)

            print('')

            print('2.Your bank balance amount =', bal[idx_id])

        else:
            print('ERROR')
            activity(idx_id)

        opt = int(input('Do you want to withdraw money (1)/deposit money (2)/log out (3) : '))

    print('logging out...')
    print('Thank You!')


acc()