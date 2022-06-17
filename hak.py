#indexes
poem = "Where am i?"

#
# print(poem[0]) #with indexes, counting from the left, the first character is always 0
#print(poem[-1]) from the right, the first character starts with -1

#slicing
#print(poem[5:]) #used to grab a change of characters from the 5th charater to the end. So, this includes the 5th character above which is the space before am

#print(poem[:4]) this one prints character from the beginning or zero to the character before the 4th. So all characters before the 4th.
#The whole point with slicing is, if the number is on the left, it is inclusive but when on the right, it is exclusive

poem1 = "Hello Pisces"
#print(poem1[-5:]) this counts from the 5th character from the right. So, theoutput will be "isces"
#print(poem1[:-5]) #this prints this prints from the beginning to the character before the 5th counting from the right. So, the 5th character is eclusive. Output will be "Hello P"

#So lets sayi want to geta particular word or number of characters together from the sentence, like "Pi"

#print(poem1[6:8]) OR
#print(poem1[6:-4]) #both will print the same

name = "Rahima Yushawu"

surname = 7       
#print(name[surname:surname+8]) #This prints the character on index 6 to index 6+8 that is 14 

#ID function

task = "Subscribe"

#print(id(task))

task = "him"

#print(id(task))

msg = "pls subscribe"

#print(len(msg)) #the len funtions is used to calculate the number of charaters or the length of the string
 
  
#print(msg[12]) #this will print the last character which is the "e" because index is always the length minus 1

"How to convert a number to a string"

msg2 = "Please subscribe"

#print("Your message was " + str(len(msg2)) + " characters long")

hi = "I like reserved guys"

#print("My confessions above has " + str(len(hi)) + " characters")

#print("My message has", (len(hi)), "characters") #this way works but will not always be available working with other funtions

#Nested Funtions
import math
age = 15

#This whole process is what was shortherned below.
age_str = str(age)
id_age = id(age_str)
other = math.floor(2.6)
added = id_age + other
added_str = str(added)
length = len(added_str)
print(length)

#print(len(str(id(str(age)) + math.floor(2.6)))) SO THIS IS THE WHOLE IDA OF NESTED FUNTIONS