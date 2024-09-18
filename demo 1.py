#Python
#basic
# n1=25
# n2=24
# res=n1+n2
#print(res)
#print(n1+n2)
#print("the sum is: ",res)
#print("the sum is n1 and n2:",res)
#print("the sum of", n1, "and", n2, "is", res)
#print("the sum {n1} and {n2}is", res)#f string

#introduction
#name="Prajwal"
#age='23'
#reg_no='054'
#ph_no='6361303689'
#email="prajwal.kumar.m.t@gmail.com"
#college="East west institute of technolgy"
#Location="Bengaluru"
#dept="Ise"
#percentage='7.27'
#print(name,'/n',age,'/n',reg_no,'/n',ph_no,'/n',email,'/n',college,'/n',Location,'/n',dept,'/n',percentage,'/n')
#print(name,'\n',age,'\n',reg_no,'\n',ph_no,'\n',email,'\n',college,'\n',Location,'\n',dept,'\n',percentage,'\n')

#str='''
#Hello, welcome to
#"Be Practical", Bengaluru
#Learning "Python Full Stack"

#print(str)

#assignment operator
"""
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("addition")
# print(x+y)
# print("---------------------------")
#
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("subtraction")
# print(x-y)
# print("---------------------------")
#
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("multplication")
# print(x*y)
# print("-----------------------------")
#
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("division")
# print(x/y)
# print("-------------------------------")
#
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("modulation")
# print(x%y)
# print("-----------------------------------")
#
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("floor division")
# print(x//y)
# print("-----------------------------------")
#
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("exponential")
# print(x**y)
# print("--------------------------------------")"""
# """
# x=int(input("enter any number::"))
# print(x**2)
#
# y=int(input("enter any number::"))
# print(y**3)"""
#
#
#
# #relation operation

# x = int(input("Enter any number:: "))
# y = int(input("Enter any number:: "))
#
# print(x>y)
# print(x<y)
# print(x==y)
# print(x!=y)
#
# """
# # arthimetic operation
#
# x = int(input("Enter any number:: "))
# y = int(input("Enter any number:: "))
#
# res=(x+y)
# print(res)
#
# res=(x-y)
# print(res)
#
# #logical operation
#
# # membership
# """
# name = 'Dawa penjor'
# print('Dawa' in name)
#
# print('dawa' in name)
#
# print('sonam' in name)
#
# print('sonam' not in name)

# #identical membership
# """
# x=[1,2,3]
# y=x
# #x=y(it shows name error)
# res=x is y
# print(res)
# print("--------------------------------------")
# a="hello"
# b="world"
# res=a is not b
# print(res)
# """
# #id() function
# """
# x=3
# y=4
# print(id(x))
# print(id(y))
# """
# #types of conversion
# """
# #implicit conversion
# x=10
# y=10.5
# print(x+y)"""
# """
# #explicit conversion
#
# #python code to demonstrate type conversion  # using int(),float()
# #initializing string
# s="10010"
# print(type(s))

# #printing string converting to int base 2
# c=int(s,2)
# print("after convertig to integer base 2: ")
# print (c)
#printing(type(c))
#printing string conerting to float
# e="8"
# e=float(8)
# print("After conerting to float:")
# print(e)
#print(type(e))
# """
# """
# #list
# my_list=['p','r','o','b','l','e','m']
# subject=['maths','science','social',['kannada','english','hindi',],'sanskrit']

# print (subject[3] [2])
# # first item
# print(my_list[0])
# #
# #second item
# print(my_list[1])
#
# #negative indexing in lists
# my_list=['p','r','o','b','e']
#
# #last item
# print(my_list[-4])
#
# print(my_list[-1])
#
# #list slicing of python
# #elements from index 2 to index 4(it will read(n-1)logic
my_list=['p','r','o','g','r','a','m']
#
# print(my_list[2:5])
#
# #negative slicing
#print(my_list[:5])
#print(my_list[-1:-5])
#
# #add/change list elements
# #correcting mistake values in a list
# even=[2,4,6,8]
# print(even)
# #change the 1st item
# even[0]=1
# print(even)
#
# even[3]=9
# print(even)
#
# #change 1st and 3rd item
# even[0:2]=3,7
# print(even)
#
# # Appending and Extending lists in python
even=[1,3,5]
# even.append([7,8,9])
# print(even)
#
# even.extend([9,11,13])
# print(even)
#
# #deleting list items
# my_list=['p','r','o','b','l','e','m']
# #deleting one item through index
# """
# """
# del my_list[2]
# print(my_list)
#
# del my_list[5]
# print(my_list)"""
#
# #delete multiple items
# """
# del my_list[1:5]
# print(my_list)
#
# #deleting entre list
# del my_list
# print(my_list)"""
#
# #remove()
# """
# my_list=['p','r','o','b',['l','u','p'],'e','m']
# my_list.remove('m')
# print(my_list)
# # #pop()
# print(my_list.pop(4))
# print(my_list)
# # #clear()
# my_list.clear()
# print(my_list)
#
# #sort python list
# #example:ascending order(default)
# """
# mylist=[21,5,8,52,21,87,52,]
# mylist.sort()
# print(mylist)
#
# #descending order
#
# mylist=[21,5,8,52,87,52]
# mylist.sort(reverse=True)
# print(mylist)
#
# #copy
# mylist=[21,5,8,52,87,52]
# mylist.copy()
# print(mylist)"""
#
# #tuples
# # changing the tuples
# """
# tpl=(2,4,5,7,8,[10,17,23],45,23)
# print(tpl)
# tpl[5][1]=27
# print(tpl)
#
# #slicing
# tpl=(2,4,5,7,8,[10,17,23],45,23)
# print(tpl)
# print(tpl[3])
# print(tpl[5][1])
# print(tpl[-3][1])"""
#
# #zipping or unzipping/pack or unpack
# """
# first_name=('Prajwal','Manoj','Cheethan')
# last_name=('Kumar','MP','Gowda')
# age=('23','22','21')
# res=zip(first_name,last_name,age)
# print(res)
# print("-------------------------------")
# student=tuple(res)
# print(student)
#
# first_name=('Prajwal','Manoj','Cheethan')
# last_name=('Kumar','MP','Gowda')
# age=('23','22','21')
# first_name,last_name,age= student [2]
# print(f"{first_name} {last_name} is {age} year old")
#
# #Adding tuples together
# #the+ operator can be used to add tuples togther
# """
# Tuple_a=(1,2)
# Tuple_b=('x','y')
# Tuple_c=Tuple_a+Tuple_b
# print(Tuple_c)
#
# a=(5,6,7,8,2)
# #a.sort
# print(type(a))
# b=sorted(a)
# print(b)"""
#
# #python set
# """
# set1=set([1,1,1,2,2,3]) #from a list
# set2=set(('a','a','b','b','c')) #from a tuple
# set3=set('anaconda') #from a string
# #second way:using curly braces
# set4={1,1,'anaconda','anaconda',8.6,(1,2,3),None}
# print('Set1::::',set1)
# print('Set2::::',set2)
# print('Set3::::',set3)
# print('Set4::::',set4)

# #clear set
# myset={1,2,3,4}
# # print(myset)
# #
# # #Removing a particlar item using the discard() method
# myset.discard(1)
# print(myset)
# myset.discard(5) #the item was absent in the set
# print(myset)
# #
# # #Removing a particular item using the remove() method
# myset.remove(4) #the item was present in the set
# print(myset)
#
# #myset.remove(5) #the item was absent in the set
# #print(myset)
#
# #taking the set from the code above
# myset={2,3,7,9}
# #removing and returning a random item
#
# print(myset.pop())#the removed and returned item
# print(myset)# updated the set
#
# myset={5,10,15,20,25}
# print('set:',myset)
# print('size:',len(myset))
# print('min:',min(myset))
# print('max:',max(myset))
# print('sum:',sum(myset))
#
# #a set with all() and any()
# print(all({1,2,'a',2.4}))
# print(all({1,False}))
# print(any({1,False}))
# print(any({False,False}))
#
# # a set with sort() function
# myset={8,9,2,7,3,4,5,}
# print(sorted(myset))
#
# #dict() function we can write in 3 type
# #type1
# MLB_team={
#     'colorado':'Rockies',
#     'Bostaon':'Red sox',
#     'Minnesota':'Twins',
#     'Milwaukee':'Brewers',
#     'Seattle':'Marines'
# }
# print(MLB_team)
#
# #type2
# MLB_team=dict([
#     ('colorado','Rockies'),
#     ('Bostaon','Red sox'),
#     ('Minnesota','Twins'),
#     ('Milwaukee','Brewers'),
#     ('Seattle','Marines')
# ])
# print(MLB_team)
#
# #type3
# #MLB_team=dict(
#  #  Bostaon='Red sox',
#   #  Minnesota='Twins',
#    # Milwaukee='Brewers',
#     #'Seattle'='Marines',
#
# #])
# #print(MLB_team)"""
# """
# Employee={"Name":"Prajwal","Age":24,"experience":4.6,"salary":25000,"company":"GOOGLE"}
#
# print(Employee)
#
#
# print("printing Employee data...")
# print("Name:%s"%Employee["Name"])
# print("Age:%d"%Employee["Age"])
# print("experience:%f"%Employee["experience"])
# print("salary:%d"%Employee["salary"])
# print("company:%s"%Employee["company"])
#
# print(Employee)"""
#
# """
# Employee={"Name":"Manoj","Age":28,"experience":7.0,"salary":50000,"company":"IBM"}
# print(Employee)
#
#
# #ADDING ONE MORE EMPLOYEE
#
# Employee={"Name":"Prajwal","Age":24,"experience":4.6,"salary":25000,"company":"GOOGLE"}
#
# print(Employee)
#
#
# print("printing Employee data...")
# print("Name:%s"%Employee["Name"])
# print("Age:%d"%Employee["Age"])
# print("experience:%f"%Employee["experience"])
# print("salary:%d"%Employee["salary"])
# print("company:%s"%Employee["company"])"""
#
# """
# Employee={"Name":"Prajwal","Age":22,"experience":4.6,"salary":25000,"company":"GOOGLE"}
# Employee['Name']='Manoj'
# Employee['Age']=24
# Employee['experience']=7.6
# Employee['salary']=65000
# Employee['company']='IBM'
#
# print(Employee)
# print("printing employee1 data:")
# print("Name:%s"%Employee["Name"])
# print("Age:%d"%Employee["Age"])
# print("experience:%f"%Employee["experience"])
# print("salary:%d"%Employee["salary"])
# print("company:%s"%Employee["company"])
# print("---------------------------------------------------")
# print("printing employee2 data:")
# print("Name:%s"%Employee["Name"])
# print("Age:%d"%Employee["Age"])
# print("experience:%f"%Employee["experience"])
# print("salary:%d"%Employee["salary"])
# print("company:%s"%Employee["company"])
#
#
#
# #Employee={"Name":"Prajwal","Age":24,"experience":4.6,"salary":25000,"company":"GOOGLE"}
#
# #print(Employee)"""
#
# """
# Employee1 = dict("Name":"Prajwal","Age":24,"Experience":4.6,"Salary":5000,"Company":"GOOGLE")
# Employee2 = dict("Name":"Manoj","Age":27,"Experience":7.6,"Salary":65000,"Company":"IBM")
#
# print(Employee1)
# print(Employee2)
#
# print employee_data(employee, employee_number):
# print("printing Employee data...")
# print("Name:%s" % Employee["Name"])
# print("Age:%d" % Employee["Age"])
# print("experience:%f" % Employee["experience"])
# print("salary:%d" % Employee["salary"])
# print("company:%s" % Employee["company"])
#
#
# print_employee_data(employee1, 1)
# print_employee_data(employee2, 2)"""
#
# # my_dict={'a':10,'b':20,'c':30}
# # print(my_dict.get('b'))
# # print(my_dict.get('a'))
#
# #d.items()
# # d={'a':10,'b':20,'c':30}
# # list(d.items())
# # print(list(d.items())[1][0])
# # print(list(d.items())[2][0])
# #
# # #key()
# # d={'a':10,'b':20,'c':30}
# #print(list(d.key()))
# #print(d.keys())
#
# #values()
# # d={'a':10,'b':20,'c':30}
# # print(d.values())
#
#
#
# #tuples
# # my_tuple = (1,'hello',3)
# # # print(my_tuple)
# # a, b, c = my_tuple
# # print(a)
# # print(b)
# # print(c)
# # tuplepl = (2, 4, 5, 7, 8, (10,17,23),45,23)
# # print('tuple'[:3])
# # print('tuple'[4:])
# # print('tuple'[-3:])
# # print('tuple'[2:5])
# # my_data = (1, 2, 3, 4, 5, 6)
# # print(my_data)
# # deleting entire tuple is possible
# # del my_data(2)
# # print('my_data')
#
#
# # my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# # print(my_data)
# # print(22 in my_data)
# # print(2 in my_data)
# # print(88 not in my_data)
# # print(101 not in my_data)
#
# # tuple_a = (1, 'x', 1, 1, 'x')
# # print(tuple_a)
# # print(tuple_a.count('x'))
# # print(tuple_a.count(1))
# ######################################################################################################
#
# #condition statement
# # x=int(input("Enter any number:"))
# # y=int(input("Enter any number: "))
# # if x>y:
# #     print(f"{x} is bigger than {y}")
# # elif x<y:
# #     print(f"{x} is lesser than {y}")
# # elif x==y:
# #     print(f"{x} is equal to {y}")
# # else:
# #     print(f"{x} is not equal  to {y}")
# ####################################################################################################################
# #WAP to find entered num is odd or even
#
# # x=int(input("Enter any number:"))
# # if x%2==0:
# #     print(f"{x} is even")
# # else:
# #     print(f"{x} is odd")
#
# #WAP to check entered year is leap year or not
#
# # x=int(input("Enter any year:"))
# # if (x%4)==0:
# #     print(f"{x} is  leap year")
# # else:
# #     print(f"{x} is  not leap year ")
#
# #WAP to check wether speicified age is valid to vote or not
# # x=int(input("Enter the age:"))
# # if x>=18:
# #     print(f"{x} is valid to vote")
# # else:
# #     print(f"{x} is not valid to vote")
#
# #WAP to check entered number is divisible by 3 or 5
# # x=int(input("enter the number:"))
# # if (x%3)==0:
# #     print(f"{x} is divisible by 3")
# #
# # elif (x%5)==0:
# #     print(f"{x} is divisible by 5")
# # else:
# #     print(f"{x} is not divisible by3 or 5")
#
# #WAP to check biggest of 3 number
# # x=int(input("enter the number:"))
# # y=int(input("enter the number:"))
# # z=int(input("enter the number:"))
# # if x>y and x>z:
# #     print(f"{x} is bigger then {y} and {z} number")
# # elif y>z and y>x:
# #     print(f"{y} is bigger then {z} and {x} number")
# # elif z>x and z>y:
# #     print(f"{z} is bigger then {x} and{y} number")
#
# #WAP to check the given alphabets is vowels or consonants
# # x=input("Enter the alphabets:")
# # if  x=="a"  and "A" or x=="e" or x=="i" or x=="o" or x=="u":
# #     print(f"{x} is the vowels")
# # else:
# #     print(f"{x} is the consonants")
#
# #WAP to 5 subject and its result
# # English=int(input("Enter the english marks:"))
# # Kannada=int(input("Enter the kannada marks:"))
# # Hindi=int(input("Enter the hindi marks:"))
# # Maths=int(input("Enter the maths marks:"))
# # Science=int(input("Enter the science marks:"))
# #
# # Total=English+Kannada+Hindi+Maths+Science
# # print(f"total marks is {Total}:")
# # Averge=Total/5
# # print(f"{Total}/5")
# # print(f"Averge marks is {Averge}:")
# # if Averge>=95:
# #     print(f"Distinction")
# # elif 65<=Averge<95:
# #     print(f"First class")
# # elif 45<=Averge<65:
# #     print(f"Second class")
# # elif 35<=Averge<45:
# #     print(f"Third class")
# # else:
# #     print(f"Fail")
# #project
# #WAP to check whether the bank account details valid or not if valid display the account details
# # id=54
# # acc_num="KAR 143"
# # Id=int(input("Enter the id of account:"))
# # Acc_num=input("Enter the acc_num: ")
# # if id==Id and acc_num==Acc_num:
# #     print('''
# #     Bank Name    : Karantaka Bank;
# #     Account holder name : Prajwal Kumar MT;
# #     Type of Account :Saving account;
# #     Account balance: 12000
# #     ''')
# # else:
# #     print(f"id={Id} or Acc_num={acc_num}")
#
# # project the rental vehicles
#
# # print("WELCOME TO PK RENTAL SHOP")
# #
# # print(("Enter your name:"))
# # Name = input("")
# # print("Enter the age:")
# # Age = int(input(""))
# # if Age < 18:
# #     print("Sorry under the 18year unable to rent the vehicle")
# #     print("Thank you  for visting our PK rental shop ")
# # else:
# #     print(input("Enter the DL.NO: "))
# #     print("""
# #     SELECT THE VEHICLE TYPE:
# #     1.TWO WHEELER
# #     2.FOUR WHEELER
# #     """)
# #
# #     Vehicle_type = int(input("Enter the vehicle type:"))
# #     if Vehicle_type == 1:
# #         print("""
# #             Two wheeler model
# #             1.KTM
# #             2.R15
# #             3.NS200
# #             4.ROYAL ENFIELD
# #             """)
# #         model = int(input("Enter the option:"))
# #         if (model == 1):
# #             print("KTM")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 50)
# #             print(cost)
# #             total = cost*0.12+cost
# #             print(total)
# #         elif (model == 2):
# #             print("R15")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 100)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         elif (model == 3):
# #             print("NS200")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 150)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         elif (model == 4):
# #             print("ROYAL ENFIELD")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 200)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         else:
# #             print("Enter vehical is invalid")
# #             print("Thanks for visting PK rental shop ")
# #
# #     #Vehicle_type = int(input("Enter the vechile type:"))
# #     #print(int(input("enter the vehicle option")))
# #     if Vehicle_type == 2:
# #         print("""
# #                       four wheeler model
# #                       1.KIA
# #                       2.HONDA
# #                       3.BMW
# #                       4.MG
# #                       """)
# #         model = int(input("Enter the option:"))
# #         if (model == 1):
# #             print("KIA")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 500)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         elif (model == 2):
# #             print("HONDA")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 1000)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         elif (model == 3):
# #             print("BMW")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 1500)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         elif (model == 4):
# #             print("MG")
# #             print("enter how many hours do you required:")
# #             hours = int(input())
# #             print("vehicle cost")
# #             cost = (hours * 2000)
# #             print(cost)
# #             total = cost * 0.12 + cost
# #             print(total)
# #         else:
# #             print("Enter vehicle is invalid")
# #             print("Thanks for visting PK rental shop ")
#
# ######################################################################################################################
# #Loops
# # for x in  range(1,11):
# #     print(x)
# #
# # for x in range(10,0,-1):
# #     print(x)
# #
# # for x in range(10,-1,-1):
# #     print(x)
# #################################################################################################################
# #WAP to find the sum of first 10 number
#
# # p=0
# # for a in range(1,11):
# #     print(a)
# #     p+=a
# # print(p)
#
#
# #WAP to print odd and even numbers between 1 to 20 and find their sum
# # sum=0
# # for x in range(1,21,):
# #     # print("enter odd number:",x)
# #     # print("enter even number:",x)
# #     if x%2==0 :
# #         print("x")
# #         print(x)
# #         sum += x
# # print("the sum of even num is:: ",sum)
# # print("______________________________")
# # if x%2!=0 :
# #     print("x")
# #     print(x)
# #     sum += x
# # print("the sum of odd num is:: ",sum)
#
# #WAP to print all leap years between 2000 and 2004
# # for x in range(2000,2025):
# #      print(x)
# #      if(x%4) == 0:
# #          print(f"{x} is   leap year ")
# #      else:
# #          print(f"{x} is  not leap year ")
# #WAP a python program that prints each item and its coressponding type from the following list
# # sample List:datalist=[1432,11.23,True,'Be Practical',(0,-1),[5,12],{"class":'V',"section":'A'}]
# # datalist=[1432,11.23,True,'Be Practical',(0,-1),[5,12],{"class":'V',"section":'A'}]
# # for i in datalist:
# #     print(f"the item is" ,{i},type(i))
#
#
# #list=[23,48,24,67,87,4,23,78]
# #WAP tp print only even number of the defind list and find their sum
# # list=[23,48,24,67,87,4,23,78]
# # sum=0
# # print(list)
# # for i in list:
# #     if i%2==0:
# #         print(i)
# #         sum += i
# #     print(sum)
#
# #WAP to print the square and cube of a given list
# # list=[2,3,4,5,6]
# # for i in list:
# #      i=i*i
# #      print(i)
# #     i=i*i*i
# #     print(i)
# #WAP to separate postive and negative number from a list
# # x=[23,4,-6,23,-9,21,3,-45,-8]
# # print(f"the postive number in{x} is ::")
# # for i in x:
# #     if i>0:
# #         print(i)
# # print(f"the negative number in{x} is ::")
# # for i in x:
# #     if i<0:
# #         print(i)
#
# #print("____________________________________________________________")
#






#WAP to print mutiplication table format of any given number
# x=16
# for i in range(1, 11):
#     print(f"{x} x {i} = {x * i}")
#
# #WAP to demonstrate a calculator
# x=int(input("Enter the any value::"))
# y=int(input("Enter the any value::"))
# print("""
# selct the sign
# 1."+"
# 2."-"
# 3."*"
# 4."/"
# 5."%"
# """)
# z=int(input("enter the option::"))
# if z== 1:
#     print('addition')
#     print(x+y)
# elif z==2:
#     print(x-y)
# elif z==3:
#     print(x*y)
# elif z==4:
#     print(x/y)
# elif z==5:
#     print(x%y)

#WAP factorial
# num=int(input("Enter  any number::"))
# fact=1
# for i in range(1,num+1):
#     fact *= i
#     #fact = fact*x
#     print(f"factorial of {num} is::",fact)

###################################################################################################################
#reverse
# num=int(input("Enter any number::"))
# rev=0
# while num!=0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# print("The reverser of the number is::",rev)
# print("---------------------------------------------------")
# num=int(input("Enter any number::"))
# rev=0
# temp=num
# while num!=0:
#     digit=num%10
#     rev=rev*10+digit
#     num//=10
# print("The reverser of the number is::",rev)
# if rev==temp:
#     print("Is Palindrome")
# else:
#     print("Is not palindrome")

#153
#1634

num=int(input("Enter any 3 digit number::"))
sum=0
temp=num
while temp>0:  #while num>0:
    digit=temp%10
    sum+=digit*digit*digit
    temp//=10

if sum== num:
    print("it is Amstrong number")
else:
    print("it is not Amstrong number")
# print("______________________________________________________")
# num=int(input("Enter any 4 digit number::"))
# sum=0
# temp=num
# while temp>0:  #while num>0:
#     digit=temp%10
#     sum+=digit*digit*digit*digit
#     temp//=10
#
# if sum== num:
#     print("it is Amstrong number")
# else:
#     print("it is not Amstrong number")
##############################################################################################################
#continue and break
# for x in range(1,21):
#     if x==14:
#         continue
#     print(x)

# for x in range(1,21):
#     if x==14:
#         break
#     print(x)

#nested of loop
# for r in range(1,6):
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()
# print("----------------------------------------------------------------")
# for r in range(5,1,-1):
#     for c in range(1,r+1):
#         print(c,end=" ")
#     print()
# print("----------------------------------------------------------------")
# for r in range(1,6):
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()
# print("-------------------------------------------------------------------")
# for r in range(1,6):
#     for c in range(1,r+1):
#         print("*",end=" ")
#     print()
# for r in range(6,1,-1):
#     for c in range(1,r):
#         print("*",end=" ")
#     print()
# print("----------------------------------------------------------------------")
################################################################################################################
#rhombus
# for x in range(6,1,-1):
#     for y in range(6,x-1,-1):
#         print(y-1,end=" ")
#     print()

# for x in range(3):
#     for i in range(1,11):
#         print(i,end=" ")
#     print("")

# rows=int(input("enter any numbers of rows::"))
# cols=int(input("enter any numbers of cols::"))
# symbols=input("enter the symbols::")
# for x in range(rows):
#     for y in range(cols):
#         print(symbols,end=" ")
#     print()

#loop with list items
# fruits=['mango','apple','grapes','peach']
# for f in fruits:
#     for i in f:
#         print(i,end="*")
#     print()

# fruits=input("Enter any fruits name::")
# for f in fruits:
#     for i in f:
#         print(i,end="*")
#     print()

# color=['red','green','pink']
# items=['apple','vigges','dress']
# for x in  color:
#     for y in items:
#         print(x,y)
#         #print()
#     print()

#while loop
# i=5
# while(i>0):
#     j=5
#     while(j>i):
#         print("*",end=" ")
#         j=j-1
#     i=i-1
#     print()

 #   Append 2 lists
# list1=[10,20,30]
# list2=[40,50,60]
# result=[]
# for i in list1:
#     for j in list2:
#         result.append(i+j)
#     print(result)

#Multipling 2 lists
# list1=[2,4,6,8]
# list2=[2,4,6,8]
# for i in list1:
#     for j in list2:
#         if i==j:
#             continue
#         print(i,"*",j,"=",i*j)

# a=1
# while a<=50:
#     sum=0
#     for i in range(1,a):
#         if i%2==0:
#             sum+=i
#     a=a+1
# print("the sum of even number is::",sum)


# fruits=['apple','mango','grapes','kiwi']
# for i in fruits:
#     count=0
#     while count<6:
#         print(i,end=" ")
#         count=count+1
#     print()

# for x in range(-6,1):
#     for y in range(-x):
#         print(y,end=" ")
#     print()

# print("welcome to rock,paper,scissor game")
# print('''
# 1.rock
# 2.paper
# 3.scissor
# ''')
# x=input("enter the option::")
# if x=='rock':
#     print("the game is over and player draw the game ")
# elif x=='paper':
#     print("the game is over and player draw the game")
# elif x=='scissor':
#     print("the game is over and player draw the game ")
# else:
#     print("the game is over and player win the game")

# num1 = 3
# num2 = 9
# print(f"The product of {num1} and {num2} is {num1 * num2}.")
# print("the product of",num1,"and",num2,"is",num1+num2)


# author = "jane smith"
# a_name = author.title()
# print(f"This is a book by {a_name}.")
#
#
# circket='doni'
# a_name=circket
# print(f"The caption of indian team is {a_name}")


# def extendlist(val,list=[]):
#     list.append(val)
#     return list
#
# list1=extendlist(10)
# list2=extendlist(123,[])
# list3=extendlist('a')
#
# print("list1=%"%list1)
# print("list2=%"%list2)
# print("list3=%"%list3)


# def extendlist(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendlist(10)
# list2 = extendlist(123, [])
# list3 = extendlist('a')
#
# print("list1=% a" % list1)
# print("list2=% a" % list2)
# print("list3=% a" % list3)


