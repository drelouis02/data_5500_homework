#2.3 variables, Math, and Output
grade = 95
print("2.3 Variables, Math, and Output")
if grade >= 90:
    gradeletter = "A"
    print(f"Congratulations! Your grade of a {grade} earns you an {gradeletter} in the course.")
    print()

#2.4 Arithmetic Operations
x = 27.5
y = 2
print("2.4 Arithmetic Operations")
print("Addition: " + str(x + y))
print("Subtraction: " + str(x - y))
print("Multiplication: " + str(x * y))
print("Division: " + str(x / y))
print("Floor Division: " + str(x // y))
print("Exponentiation: " + str(x ** y))
print()

#2.5 Circle Area, Diameter, and Circumference
pi = 3.14159   
radius = 2
diameter = 2 * radius
area = pi * (radius ** 2)
circumference = 2 * pi * radius 
print("2.5 Circle Area, Diameter, and Circumference")
print(f"Circle with radius {radius}:")
print(f"Diameter: {diameter}")  
print(f"Area: {area}")
print(f"Circumference: {circumference}")
print()

#2.6 Odd or Even
integer =  input("2.6 Odd or Even\nEnter an integer: ")
if int(integer) % 2 == 0:
    print(f"{integer} is an even number.")
else:
    print(f"{integer} is an odd number.")
print()

#2.7 Multiples
first_number = 1024
second_number = 2
print("2.7 Multiples")
if first_number % 4 == 0:
    print(f"{first_number} is a multiple of 4.")
else:
    print(f"{first_number} is not a multiple of 4.")
if second_number % 10 == 0:
    print(f"{second_number} is a multiple of 10.")
else: 
    print(f"{second_number} is not a multiple of 10.")
print()

#2.8 Table of Squares and Cubes
print("2.8 Table of Squares and Cubes")
print("Number\tSquare\tCube")
for i in range(0, 6):
    square = i ** 2
    cube = i ** 3
    print(f"{i}\t{square}\t{cube}")
print() 

#3.4 Double For Loop
print("3.4 Double For Loop")
for i in range(2):
    for j in range(7):
        print("@", end="")
    print()
print()

#3.9 Seperate Digits of an Integer
print("3.9 Separate Digits of an Integer")
integer_for_separation = input("Enter an integer between 7 and 10 digits: ")
integer_for_separation = int(integer_for_separation)
combined_digits = ""
for i in range(len(str(integer_for_separation))):
    digit = int(integer_for_separation - (integer_for_separation % (10 ** (len(str(integer_for_separation)) -1))))/(10 ** (len(str(integer_for_separation)) -1))
    print(int(digit))
    integer_for_separation = integer_for_separation % (10 ** (len(str(integer_for_separation)) -1))
print()


#3.11 Miles per Gallon
print("3.11 Miles per Gallon")
gallons_used = float(input("Enter the number of gallons of gas used (-1 to end): "))
miles_driven = float(input("Enter the number of miles driven: "))   
total_miles = 0
total_gallons = 0
while gallons_used != -1:
    mpg = miles_driven / gallons_used
    total_miles += miles_driven
    total_gallons += gallons_used
    print(f"Miles per gallon: {mpg:.2f}")
    gallons_used = float(input("Enter the number of gallons of gas used (-1 to end): "))
    if gallons_used == -1:
        break
    miles_driven = float(input("Enter the number of miles driven: "))
print()
print(f"Total miles driven: {total_miles}")
print(f"Total gallons used: {total_gallons}")   
print(f"Overall miles per gallon: {total_miles / total_gallons:.2f}")
print()

#3.12 Plaindromes
print("3.12 Palindromes")
digits_reversed = []
five_digit_number = input("Enter a five-digit integer: ")
for i in range(5):
    digit = five_digit_number[4 - i]
    digits_reversed.append(digit)
if digits_reversed == list(five_digit_number):
    print(f"{five_digit_number} is a palindrome.")
else:
    print(f"{five_digit_number} is not a palindrome.")
print()

#3.14 Approximating the Mathematical Constant Pi
#To get to 3.14 it takes approximately 627 terms of the series
#To get to 3.141 it takes approximately 2458 terms of the series
print("3.13 Approximating the Mathematical Constant Pi")
subtracting_number_denominator = 3
adding_number_denominator = 5
running_diff_number = 4
pi = 4
for n in range(1, 3001):
    if n % 2 == 0:
        pi = pi + (4/adding_number_denominator) 
        adding_number_denominator += 4
    else:
        pi =  pi - (4/subtracting_number_denominator)  
        subtracting_number_denominator += 4
    print(f"Approximation of pi after {n} terms: {pi:.6f}")