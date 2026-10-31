print("Enter your Details Below: ")
name = input("Name: ")
# int will only allow integer values any other value we get error 
age = int(input("Age: ")) # type casting string to integer 
# float will accept both int values and float values 
height = float(input("Height: "))# type casting string to float 
# str() , bool() 
gender = input("Gender: ")
print("Student Details: ")
print("="*15)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Gender: {gender}")

