'''Activity 1'''
from fractions import Fraction
from xmlrpc.client import boolean

denominator = 2
result = Fraction(0, 1)
for i in range(1, 100):
    result = Fraction(1, denominator) + result
    denominator *= 2
print(f"Final result: {result}")

'''Activity 2 '''
colors = ["red", "blue", "green", "yellow", "orange"]
for color in colors:
    print(color)

'''Activity 3'''
for color in colors:
    for i in color:
        print(i)

'''Activity 4'''
from random import randint
random_number = randint(1, 100)
int_list = []
for _ in range(10):
    int_list.append(randint(1, 100))
print(f"Random numbers: {int_list}")

'''Activity 5'''
for i in range(len(int_list) - 1):
    if int_list[i] % 2 == 0 and int_list[i + 1] % 2 == 0:
        print(int_list[i], int_list[i + 1])

'''Activity 6'''
for i in range (2 , 101):
    if i % 2 == 0:
        print(i)

'''Activity 7'''
list_of_strings = ["apple", " banana", " cherry", " date", "elderberry  "]
cleaned_strings = [item.strip() for item in list_of_strings]
print(cleaned_strings)

'''Activity 8'''
child_age = input("How old is your child? ")
child_weight = input("How much does your child weigh? ")
front_seat_allowed = False

if int(child_age) >= 12:
    front_seat_allowed = True
elif int(child_age) == 11 and int(child_weight) > 90:
    front_seat_allowed = True
elif int(child_age) < 11 and int(child_weight) > 100:
    front_seat_allowed = True
else:
    front_seat_allowed = False

    
if front_seat_allowed:
    print("Your child is allowed to sit in the front seat.")
else:
    print("Your child is not allowed to sit in the front seat.")