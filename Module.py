#regular expression
#search () example
# import re
# message = "I like Football"
# x=re.search("F",message)
# print(x.start())
#
# print("______________________________________________________________________________")
# #findall() example
# import re
# message="Hagi is a perfect footballer.Hagi is from Romanina"
# x=re.findall("Hagi",message)
# print(x)
# print("______________________________________________________________________________")
# #split() example
# import re
# message = "I like Football"
# x=re.split("\\s",message)
# print(x)
# print("______________________________________________________________________________")
#
# message="I like football basketball volleyball"
# x=re.split("\\s",message,2)
# print(x)
# print("______________________________________________________________________________")
#
# #sub() example:
# message='I like Football'
# x=re.sub("\\s","-",message)
# print(x)
# print("______________________________________________________________________________")
# message="I like football"
# x=re.sub("\\s","-",message,1)
# print(x)
# print("______________________________________________________________________________")


import re
# pattern="Python"
# text="I write code in Python"
# match=re.search(pattern,text)
# print("Match found :", bool(match))
# print("______________________________________________________________________________")
# pattern="Python"
# text="I write code in python"
# match=re.search(pattern,text)
# print("Match found :", bool(match))
# print("______________________________________________________________________________")
#
# pattern ="a"
# text="I love to code in Python and it's amazing!"
# match=re.findall(pattern,text)
# print("Match found:", len(match))
# print("______________________________________________________________________________")
#
# pattern="\s"
# text="I like python and it's is amazing!"
# split_text=re.split(pattern,text)
# print("split text :", split_text)
# print("______________________________________________________________________________")
#
# pattern="Python"
# replacement="java"
# text="Python is fun"
# substitution_text=re.sub(pattern,replacement,text)
# print("substitution text:",substitution_text)
# print("______________________________________________________________________________")
#
#
# #using * to match zero or more occurrences of a character
# pattern="Py.*n"
# count=0
# text=["Python coding","Pyt3on","Java","Py45n","Py@#n","Pyn"]
# for i in text:
#     if(re.findall(pattern,i)):
#         count+=1
# print("Matches found:",count)
# print("______________________________________________________________________________")
#
# #using + to match zero or more occurrences of a character
# pattern="Py.+n"
# count=0
# text=["Python coding","Pyt3on","Java","Py45n","Py@#n","Pyn"]
# for i in text:
#     if(re.findall(pattern,i)):
#         count+=1
# print("Matches found:",count)
# print("______________________________________________________________________________")

#using ? to match zero or more occurrences of a character
# pattern="Py.?n"
# count=0
# text=["Python coding","Pyt3on","Java","Py45n","Py@#n","Pyn"]
# for i in text:
#     if(re.findall(pattern,i)):
#         count+=1
# print("Matches found:",count)
# print("______________________________________________________________________________")
#
#
#
# #using [] to create a character set
# pattern="[Pp]ython"
# text="I write code in python and Python!"
# matches=re.findall(pattern,text)
# print("Matches found:",len(matches))
# print("______________________________________________________________________________")
#
# #using {} to specify the number of occurences of a character
# pattern="Py{1,2}n"
# text="I love Pyn,Pyyn, and Pyyyn!"
# matches=re.findall(pattern,text)
# print("Matches found:",len(matches))
# print("________________________________________________________________")
#
# #using \d to matches digits
# pattern ="\d+"
# text="my phone number is 123-456-7890-123456."
# matches=re.findall(pattern,text)
# print(matches)
# print("Matches found:",len(matches))
# print("________________________________________________________________")

#using \w to match alphanumeric characters
# pattern="\w+"
# text="I_love_Python!"
# matches=re.findall(pattern,text)
# print(matches)
# print("Matches found:",len(matches))
# print("________________________________________________________________")

#using \s to match whitespace characters
# pattern="\s+"
# text=" I love python!"
# matches=re.findall(pattern,text)
# print(matches)
# print("Matches found:",len(matches))
# print("________________________________________________________________")
#
# #using | as an OR operator
# pattern="Python|Java"
# text="I write code in Python and Java!"
# matches=re.findall(pattern,text)
# print(matches)
# print("Matches found:",len(matches))
# print("________________________________________________________________")

#using ()  to group patterns
# pattern="(\d{3})-(\d{3})-(\d{4})"
# text="My phone number is 123-456-7890"
# match=re.findall(pattern,text)
# #print(match)
# if matches:
#     print("area code:",match.group (1))
#     print("local exchange:",match.group (2))
#     print("line number:",match.group (3))
# print("_______________________________________________________________________")

# import glob
# print(glob.glob('*.py'))