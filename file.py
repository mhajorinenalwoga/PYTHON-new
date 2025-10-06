#print("Hello Python")
#print("#" * 10)
#print ('hello')
#x = 10
#y = 20
#unitprice = 3.45
#an expression
#x + y * 2

#Variables is an entity we use to store information in computer memory
student_count = 1000 #interger
rating = 4.99 #float
is_published = True #boolean
course_name = "Python Programming" #string
hash(course_name)#hash value of the string
#hash("hello") works in cmd and not vscode
#a function is a reusable piece of code that performs a specific task
length = len(course_name) #len is a function that returns the length of a string
print(length)
print(course_name[0])#indexing first character
print(course_name[-1]) #indexing last character
print(course_name[0:3])#indexing first three characters
print(course_name[0:]) #indexing from first character to the end
print(course_name[:3]) #indexing from the start to the third character
print(course_name[:]) #indexing the entire string

#\" is used to escape double quotes in a string
course_description = "This course is designed to teach you the basics of \"Python Programming\""
print(course_description)

#\' is used to escape single quotes in a string
course_description2 = 'It\'s a great course'    
print(course_description2)

#\\ is used to escape backslashes in a string
file_path = "C:\\Users\\User\\Documents\\file.txt"
print(file_path) 

#\n is used to insert a new line in a string
course_description3 = "This course is designed to teach you the basics of Python Programming.\n"
"It is a great course for beginners."
print(course_description3)

first = "Majorine"
last = "Nalwoga"
full = first + " " + last
full = f"{first} {last}" #f-string
print(full)

food = "Chips and chicken"
print(food.upper()) #upper case
print(food.lower()) #lower case
print(food.title()) #title case
print(food.strip()) #remove whitespace
print(food.replace("Chpis", "Fries")) #replace
print(food.find("And")) #find index of a substring
print("chi" in food) #check if a substring is in a string
print("pizza" not in food) #check if a substring is not in a string






