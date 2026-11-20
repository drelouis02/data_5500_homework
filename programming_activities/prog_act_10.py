#Activity 1
#ask for two numbers and store them as integers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#create a list to store the multiplication table
table = []
#create a nested loop to generate the multiplication table
for i in range(1, num1 + 1):
    row = []
    for j in range(1, num2 + 1):
        row.append(i * j)
    table.append(row)
# print the multiplication table
print("Multiplication Table:")
for row in table:
    for value in row:
        print(value, end = " ")
    print()  # Move to the next line after each row

# Activity 2
#ask for age and favorite color and store them in a dictionary
age = int(input("Enter your age: "))
favorite_color = input("Enter your favorite color: ")
#have the dictionary store the multiplication table as well
person = {"age": age, 
          "favorite_color": favorite_color,
          "multiplication_table": table}
#print the dictionary values
for key in person:
    print(f"{person[key]}")

#Activity 3
import json 

#open person.json and load it into a dictionary
with open("person.json", "r") as file:
    person_data = json.load(file)   

#add 1 to all person["age] 
person_data["age"] += 1
#save updated dictionary to person.json
with open("person.json", "w") as file:
    json.dump(person_data, file, indent=4)

#open person.json and print the updated dictionary
with open("person.json", "r") as file:
    updated_person_data = json.load(file)
    print(updated_person_data)

# Activity 4
#ask for two numbers and store them as floats
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#create try and except block to catch ZeroDivisionError
try:
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: attempted to divide by zero.")
