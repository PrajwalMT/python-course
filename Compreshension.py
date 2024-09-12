#normal with list
# city1=["Paris","Landon","Berlin","Tokyo","Sydney"]
# city2=[]
# for x in city1:
#     city2.append(x)
# print(city2)
# print("___________________________________________________________")
# #with list comprehension
# city1=["Paris","Landon","Berlin","Tokyo","Sydney"]
# city2=[]
# city2=[x for x in city1]
# print(city2)
# print("___________________________________________________________")
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_no=[]
# even_no=[x for x in numbers if x%2==0]
# print(even_no)
# print("___________________________________________________________")
# #normal
# list1=['q','a','t','d','o','f','e']
# list2=['a','e','i','o','u']
# result=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             result.append(i)
# print(result)
# print("___________________________________________________________")
# #with list comprehension
# list1=['q','a','t','d','o','f','e']
# list2=['a','e','i','o','u']
# result=[i for i in list1 for j in list2 if i==j]
# print(result)
# print("___________________________________________________________")
#
# words=['Filtering','words','based','on','length']
# five_lttr=[word  for  word in words if len(word)==5]
# print(five_lttr)
# print("___________________________________________________________")
#
# my_fruit=['Apple','Banana','Orange','Mango']
# my_fruit2=[i[0] for i in my_fruit]
# print(my_fruit2)
# print("___________________________________________________________")
#
# mixed_list=['Apple','Banana','12','15','7','2','3','Orange','Mango']
# #if type is equal to int then apppend square of the number
# #otherwise append first character of string
# mixed_list2=[i**2 if type(i)==int else i[0] for i in mixed_list]
# print(mixed_list2)
# print("___________________________________________________________")
# #normal
# def power(x):
#     return x**2
# p_num=[]
#
# for x in range(1,10):
#     p_num.append(power(x))
# print(p_num)
# print("___________________________________________________________")
#
# #with nested list comprehension
# res=[(x,y) for x in [1,2,3]for y in [3,4,1]if x!=y]
# print(res)
# print("___________________________________________________________")
# nsted=[[1,2],[3,4],[5,6]]
# elements=[elements for pair in nsted for elements in pair]
# print(elements)
# print("___________________________________________________________")
# list1=[1,2,3]
# list2=['a','b','c']
# pairs=[(x,y) for x in list1 for y in list2]
# print(pairs)
#
#
# print("========================Questions================================================")
# #1.Generate a set of comman elements from two lists
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# #result=[i for i in list1 for j in list2 if i==j]
# result=[(x,y)for x in list1 for y in list2 if x==y]
# print(result)
# print("___________________________________________________________")
# #2.WAP to generate paris of distinct elements and their character position sum from two lists
# list1=["abc","def","ghi"]
# list2=["jkl","mno","pqr"]
# #pairs=[i**2 if type(i)==int else i[0] for i in list1]
# pairs=[(i,j) for i in list1 for j in list2 ]
#
# print(pairs)
# print("___________________________________________________________")
# #3.create pairs of distinct elements and their absolute difference from two
# list1=[3,6,9]
# list2=[5,10,15]
# pairs=[(x,y,abs(x-y))for x in list1 for y in list2 if x!=y]
#
# print(pairs)
# print("___________________________________________________________")
# #4.Write  a list compreshension display number and their binary representation from 1 to 10
# binary=[(n,bin(n)) for n in range(1,11)]
# print(binary)
# print("___________________________________________________________")
# #5.Write  a list compreshension of number and their  factorial from 1 to 10
# import math
# numbers_and_factorials = [(n, math.factorial(n)) for n in range(1, 11)]
# print(numbers_and_factorials)

# print("***********************************SET COMPREHENSION******************************************************")
# words=['apple','banana','cherry','pmpkn']
# vowels={'a','e','i','o','u'}
# vowels_words={word for word in  words if any(letter in vowels for letter in word)}
# print(vowels_words)
# print("___________________________________________________________")
# mylist=[1,2,3,4,5,6,7,8,9,10]
# newset={element*3 for element in mylist}
# print("the existing list is:",mylist)
# print("the newly created set is:",newset)
# print("___________________________________________________________")
# mylist=[1,2,3,4,5,6,7,8,9,10]
# newset={element**2 for element in mylist}
# print("the existing list is:",mylist)
# print("the newly created set is:",newset)
# print("___________________________________________________________")
# fear='the only thing we have to fear is fear itself'
# res=len({w for w in fear.split() if 't' not in w})
# print(res)
# print("___________________________________________________________")
# #set of reversed strings from another set
# words={"apple","banana","cherry"}
# reversed_words={word[::-1]for word in words}
# print(reversed_words)
# print("___________________________________________________________")
# #to get only digits from the string
# string="12345Hello67890"
# digits={char for char in string if char.isdigit()}
# print(digits)
# print("________________________________________________________________")
# numbers=[1,2,3,4,5]
# squared_numbers={x**2 for x in numbers}
# print(squared_numbers)
# print("____________________________________________________________________")
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i ==0:
#             return False
#     return True
# prime_number={x for x in range(1,51)if is_prime(x)}
# print(prime_number)
# print("____________________________________________________________________")
# #set of even numbers squared and odd numbers cubed from 1 to10
# result={x**2 if x % 2 == 0 else x**3 for x in range(1,11)}
# print(result)
# print("____________________________________________________________________")
# #set of unquie number from a list
# numbers=[1,2,3,2,4,5,1]
# unquie_number={x for x in numbers}
# print(unquie_number)
# print("____________________________________________________________________")
# #set of square roots from a set of numbers
# import math
# num={1,4,9,16,25}
# num_sqrt={math.sqrt(x) for x in num}
# print(num)
# print(num_sqrt)
# print("____________________________________________________________________")
#
# print("**********************************Dict comprehension****************************************")
# #dictionary of square of number from 1 to 10
# squares={x:x**2 for x in range(1,11)}
# print(squares)
# print("____________________________________________________________________")
# #dictionary of even numbers as keys and their squares as values
# even_squared={x:x**2 for x in range(0,21 )if x %2==0}
# print(even_squared)
# print("____________________________________________________________________")
#
# #dictionary of words and their lengths from a sentence
# words="Python is awesome"
# word_lengths={word:len(word) for word in words.split()}
# print(word_lengths)
# print("____________________________________________________________________")
# #dictionary of numbers and their cubes
# numbers=[1,2,3,4,5]
# cubes={x:x**3 for x in numbers}
# print(cubes)
# print("____________________________________________________________________")
# #dictionary of numbers and their prime values
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# numbers=[1,2,3,4,5,6,7,8,9,10]
# prime_status={x:is_prime(x) for x in numbers}
# print(prime_status)
# print("____________________________________________________________________")
# #dicitonary of words and the count of vowels from a list of strings
# words=['apple','banana','cherry']
# vowel_count={word:sum(1 for char in word if char.lower() in 'aeiov')for word in words}
# print(vowel_count)
# print("____________________________________________________________________")
# #dictionary of words and their reversed forms
# words=['apple','banana','cherry']
# reversed_words={word:word[::-1] for word in words}
# print(reversed_words)
# print("____________________________________________________________________")
# #create a dictionary of number and their parity (even or odd)
# numbers=[1,2,3,4,5,6,7,8,9,10]
# pair_num={x:'even' if x%2==0 else 'odd' for x in numbers}
# print(pair_num)
# print("____________________________________________________________________")
# #create a dictinory of numbers and their factoeials
# import math
# numbers_and_factorials = [(n, math.factorial(n)) for n in range(1, 11)]
# print(numbers_and_factorials)
# print("____________________________________________________________________")

print(int(eval(input("Enter calucater: "))))
