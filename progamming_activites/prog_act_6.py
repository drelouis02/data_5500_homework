# Activity 1
# Define a function that takes a name as an argument
def welcome_fctn(name):
    # Print a welcome message using the provided name
    print(f"Welcome, {name}!")

# Call the function with a name
welcome_fctn("Alice")


# Activity 2
# Define a function that takes a name and returns a welcome message
def welcome_fctn(name):
    # Store the welcome message in a variable
    welcome_message = "Welcome " + name

    # Return the welcome message
    return welcome_message

# Call the function and print the returned message
print(welcome_fctn("Andre"))


# Activity 3
# Define a function that accepts a name, age, and favorite color
def welcome_fctn(name, age, favorite_color):
    # Concatenate the arguments into a welcome message
    # Convert age to a string so it can be combined with text
    welcome_message = "Welcome " + name + ", you are " + str(age) + " years old, and " + favorite_color + " is your favorite color"

    # Return the completed welcome message
    return welcome_message

# Call the function with three arguments and print the result
print(welcome_fctn("Andre", 23, "Blue"))


# Activity 4
# Import NumPy to work with arrays
import numpy as np

# Create a NumPy array containing 100 zeros
numbers = np.zeros(100)

# Replace all zeros with random decimal values between 0 and 1
numbers[:] = np.random.rand(100)

# Print the updated array of random numbers
print(numbers)