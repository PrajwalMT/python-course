# #(lambda a,b :a * b)(5,6)
# x=lambda a,b : a* b
# print(x(5,6))
#
# name_list=['Grace Hopper','Ada Lovelace','Emmy noether','Marie Curie']
# sorted_by_surname=sorted(name_list,key=lambda x: x.split( )[1])
# print(sorted_by_surname)
#
# def add(a,b):
#     return (lambda x: a+b)
# f=add(3,4)(0)
# print(f)
#
# res=lambda x:(x%2 and 'odd'or 'even')
# print(res(16))
#
# str=lambda string:string in "Welcome to the world of Lambda Function in Python"
# print(str('Python'))

#map with upper()
# lst=['prajwal','manoj','chethan','bharath']
# lst_upper_case=list(map(str.upper,lst))
# print(lst_upper_case)
#
# #round()
# circle_areas=[3.56789,5.25494,4.354894,5.3539,9.24248,3.354]
# res=list(map(round,circle_areas,range(1,7)))
# print(res)
#
#normal
# strngs=['a','b','c','d','e']
# num=[1,2,3,4,5]
#
# res=list(zip(strngs,num))
# print(res)

# #using lambda
# strngs=['a','b','c','d','e']
# num=[1,2,3,4,5]
# res=list(map(lambda x,y:(x,y),strngs,num))
# print(res)

# marks=[45,50,60,55,65,70,75,80,85,90]
# def sort_marks(marks):
#     return marks>70
# res=list(filter(sort_marks,marks))
# print(res)
#
# words=['hgflkjh','madam','mom','radar','mnbv']
# palindrome=list(filter(lambda word:word==word[::-1],words))
# print(palindrome)


#double of each number using map function
# numbers=[1,2,3,4,5]
# double_number=list(map(lambda x:x*2,numbers))
# print(double_number)

#normal
# from functools import reduce
# numbers=[1,2,3,4,5,6]
# print(numbers)
#
# def cust_sum(first,second):
#
#     return first+second
# result=reduce(cust_sum,numbers)
# print(result)
#
# #using lambda
# numbers=[1,2,3,4,5,6]
# total=reduce(lambda x,y:x+y,numbers)
# print(total)
#
#
# numbers=[1,7,3,9,5]
# max_number=reduce(lambda x,y:x if x>y else y,numbers)
# print(max_number)

