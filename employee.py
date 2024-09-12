# print("Employee details as Traniee,Manager,HR")
# choice=int(input("Enter the option:::"))
# if choice<5:
#
#     print("he is the traniee")
#
# elif choice>5:
#
#     print("he\she is a Manager")
#
# elif choice>10 and choice>15:
#     print("he\she is a HR ")
# else:
#     print("")

# Function to determine role based on years of experience
# def determine_role(years_of_experience):
#     if years_of_experience < 2:
#         return "Trainee"
#     elif 2 <= years_of_experience <= 5:
#         return "Manager"
#     elif years_of_experience > 5:
#         return "HR"
#     else:
#         return "Invalid input"
#
# # Input from user
# try:
#     experience = float(input("Enter the number of years of experience: "))
#     role = determine_role(experience)
#     print(f"The role is: {role}")
# except ValueError:
#     print("Please enter a valid number.")
#
# # Example of usage
# # You can also call the function directly like this:
# # print(determine_role(3))  # Output: Manager

# a = """ IM learning
# python to develop
# an application
# """
#
# print(a)

# a = True
# b = False
# print("a and b is", a and b)
# x=2
# y = 3
# c=x & y
# print(c)

float_var = 56.78
int_var = 123
str_var = "123.2"

# res_int = int(float_var)
# print(res_int)
# print("Type: ", type(res_int))

# res_str = str(float_var)
# print(res_str)
# print("Type: ", type(res_str))

# res_ftr = float(str_var)
# print(res_ftr)
# print("Type: ", type(res_ftr))

# c = int(s,2)
# print ("After converting to integer base 2 : ")
# print (c)
# print(type(c))

# my_list = ['p','r','o','b','e']
#
# # last item
# print(my_list[-1])
my_list = ['p','r','o','g','r','a','m','m','i','i','n','g']
# print(len(my_list))
# print(my_list[2:5])
# print(my_list[5:])
# print(my_list[  : -6 ])
# even = [1, 3, 5]
# even.append([7,8,9])
# even.extend([9, 11, 13])
# print(even)

# cars = ['Ford', 'Volvo', 'BMW', 'Tesla']
# #some updates on list
# cars.append('Honda')
# cars.append('Tata')
# print(cars)
# #find length of list
# length = len(cars)
# print('Length of the list is :', length)
mylist = [21, 5, 8, 52, 21, 87, 52]

#reverse list
mylist.reverse()
#print the list
print(mylist)
print("=========================================")
mylist = [21, 5, 8, 52, 21, 87, 52]
#reverse list using slicing
mylist = mylist[::-2]
#print the list
print(mylist)

a, b, c = my_tuple
print(a)
print(b)
print(c)



