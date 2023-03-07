#!/bin/python3

#STRINGS

print ("Hello Worlds!")
print ("Hello Worlds!")
print("""This stirng runs
multiple lines!""") #triple quote for multi-line
print("This string is "+"awesome!") #We can also concatenate
print ('\n') #new line
print('Test that new line out.')


print ('\n') #new line
#MATH

print(50+50) #add
print (50-50) #sub
print(50*50) #multiply
print(50/50) #divide
print(50**2) #exponent
print(50% 6) #modulo - takes what is left over
print(50/6) #division with remainder (or a float)
print(50 //6) #no remainder

print ('\n') #new line
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts chars

name = "Troy" #stirng
age = 31 #int
gpa = 3.7 #float - has decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #will it round? no

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print ('\n') #new line
#FUNCTIONS

def who_am_i(): #this is a function without params
	name = "Troy"
	age = 31
	print("My name is " + name + " and I am " + str(age) + "years old.")

who_am_i()

def add(x,y):
	print(x+y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x**.5)
	
square_root(64)

def nl(): #new line
	print('\n')
	
nl()

# BOOLEAN EXPRESSIONS AND RELATIONAL OPERATORS
## BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))


nl()

## RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >=7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 < 7) #True

test_not = not True #False

nl()

#CONDITIONAL_STATMENTS - if/else

def drink(money):
	if money >=2:
		return "You get a drink"
	else:
		return "No drink!"
		
print(drink(3))
print(drink(1))

nl()

def alcohol(age,money):
	if (age >=21) and (money >=5):
		return "Get a drink"
	elif (age >=21) and (money <5):
		return "You're broke."
	elif (age < 21) and (money >=5):
		return "You're a kid!"
	else: 
		return "You're too young and too poor."
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()

#LISTS - have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "Exorcist"]

print(movies[1]) #returns the 2nd item
print(movies[0]) #returns 1st item
print(movies[1:3]) #return the first index number given untuul the last number, but not include the last number
print(movies[1:])
print(movies[:1])
print(movies[-1]) #return last item in the list

print(len(movies)) #count items in list

movies.append("JAWS")
print(movies) #appends to the end of the list

movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes the last item
print(movies)

grades = [["Bob" , 82 ], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)

nl()
# TUPLES - Do not change ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
#LOOPING

#For Loops - start to finish of an iterate
vegetables = ["cucumebr", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
#While Loops - execute as long as True
i = 1

while i < 10:
	print(i)
	i += 1

nl()

# ADVANCED STRINGS

my_name = "Troy"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter -default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
       
quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money\""
print (quote)  
       
too_much_space = "                hello               "
print(too_much_space.strip())

print("A" in "Apple")
print("a" in "Apple")

letter = "A"
word = "Apple" 

print(letter.lower() in word.lower()) #improved  
       
movie = "The Hangover"
print("My Favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favoirte movie is {movie}.")

nl()

# DICTIONARIES - key/value pairs {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8} #drink is the key, price is the value
print(drinks)
       
employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Lousie", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)


employees.update({"Sales":["Andie", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
