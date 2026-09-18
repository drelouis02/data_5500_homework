'''1'''
apple_price = 1.83
number_purchased = 16
tax = 1.07
total_bill = apple_price * number_purchased * tax
if total_bill == 0:
    print ("Check to make sure imputs are correct")
print(f"The total bill is ${total_bill:.2f} and you purchased {number_purchased} apples")

"""2"""
age = input("How old are you? ")
desired_age = input("What age would you like to be? ")
years_left = int(desired_age) - int(age)
print(f"You have {years_left} years left until you are {desired_age} years old.")

'''3'''
user_score = input("What is your score in this class? ")
user_score = int(user_score)
if user_score >= 93:
    print("Congratulations you got an A!")
else:
    print("Congratulations, you still learned a ton!!!!")

'''4'''
year_born = input("What year were you born? ")
if int(year_born) > 1997:
    print("You are a zoomer")
elif int(year_born) > 1981 and int(year_born) < 1997:
    print("You are a millennial")
elif int(year_born) > 1965 and int(year_born) < 1981:
    print("You are a Gen X")
elif int(year_born) > 1946 and int(year_born) < 1965: 
    print("You are a baby boomer")
else:
    print("You are a very old person, make sure to take care of yourself and stay healthy!")


'''5'''
from datetime import datetime
current_year = datetime.now().year
user_age = input("How old are you? ")
while int(user_age) >= 1:
    print(f"You were alive in {current_year}")
    user_age = int(user_age) - 1
    current_year = int(current_year) - 1

'''6'''
for i in range(5, 96, 5):
    print(i)

'''7'''
i = 5
while i < 96:
    print(i)
    i += 5

'''8'''
three_digit_number = input("Please enter a three digit number: ")
three_digit_number = int(three_digit_number)    
first_digit = three_digit_number // 100
third_digit = three_digit_number % 10
if first_digit == third_digit:
    print("Palindrome!!")
else:
    print("Not a palindrome :(")