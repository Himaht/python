####LISTS#####

ages = [12, 22, 25]

students = ["Fulera", "Ayi", "Amina"]

favorites = ["Netflix", 18, ["Hakim", "Sweet"]]

#LISTS ARE MUTABLE- WE CAN CHANGE THEM WITHOUT CREATING A NEW ONE 

print(id(favorites))

favorites[0] = "Cooking"

print(id(favorites))
#the ID before and after the change in list remains the same since it was just the data which was changes but not create a new object in memory
print(favorites)

#length of list

#print(len(favorites)) #this will print 3 because Hakim and Sweet combine as 1 character

###COPYING A LIST### this is done if you want to modify a list but kepp the original copy

favorites = ["Netflix", 18, ["Hakim", "Sweet"]]

#print(favorites[0:1]) #this will print ['Netflix]- slicing rule

#print(favorites[:]) #this prints the same list

copy = favorites[:]
#print(copy)

copy[0] = "Food"

#print(favorites, copy)

cities = ["Accra", "Tamale", "Tema"]

carbon = cities[:]

carbon[1] = "Yendi"

#print(cities, carbon)

#Nested lists
foods = ["TZ", "Waakye", ['egg', 'spagetti',['stew', 'shitto']]]

#print(foods[2][1])

sweet = ["him", 7, "Dee", ["me", "you",["them", "him"]]]

#print(sweet[3][2]) 

copy1 = sweet.copy()

copy1[1] = 8

#print(sweet, copy1)

##DEEP COPYING###
import copy
from statistics import linear_regression 

my_favorite_people = ["Fulera", "Yushawu",["Khasiyat", "Chenti", "Aslam",["Hakim, Sweet"]]]

c3 = copy.deepcopy(my_favorite_people)

c3[2][0] = "Alhaj" 

#print(my_favorite_people, c3) 

#Combining List#

my_best = ["Food", "Drink", ["Mom", "Ayuba", "Rashud"]]

least_fav = ["Lies", "Reptiles"]
print(my_best + least_fav)

#To add to a list, you ca do the following below

#least_fav = least_fav + ["him"] #####OR

least_fav.append("him")
print(least_fav)