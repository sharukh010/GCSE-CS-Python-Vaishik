# single line comment 
"""
this 
is 
an example 
of multi line comment 
"""

# store details of a person 
name = "vaishik" # string 
age = 16 # int 
height = 5.756  #in feet # float
#1st way to store gender 
# gender = "male" # "female"
#2nd way to store gender 
is_male = True  
print("Student Details: ")
# whenever you pass multiple values in print it will be printed seperated by spaces 
# print("Name:",name)
# print("Age:",age)
# print("Height:",height)
# print("Is Male:",is_male)

print(f"Name: {name}")
print(f"Age: {age}")
"""
.1f will round it up to nearest 1 decimal point 
.2f will give only 2 digits after decimal point 
.0f will round up the value and give an interger 
"""
print(f"Height: {height:.2f}")
print(f"Is Male: {is_male}")

