# Programming Activity 1
#open the file
file = open("AAPL.2023.txt", "r")
#make two distinct counts for both answers
total = 0
count = 0

first_5_total = 0
first_5_count = 0
#for loop to read each line in the file and strip the whitespace and convert to float
for line in file:
    number = float(line.strip())

    # Total for all days
    total += number
    count += 1

    # Total for first 5 days only
    if first_5_count < 5:
        first_5_total += number
        first_5_count += 1

file.close()

# Calculate averages
average = total / count
average_5_days = first_5_total / first_5_count

print(f"Average: {average}")
print(f"Average for first 5 days: {average_5_days}")







# Programming Activity 1.2

print()
print()

# Open the file
file = open("AAPL.2023.txt", "r")

# Create a list to store the numbers
numbers = []

# Store buy/sell signals and the days they happen
signal = []
signal_days = []

for line in file:
    number = float(line.strip())
    numbers.append(number)

file.close()


# Create total and average for first 4 days
first_4_total = sum(numbers[:4])
first_4_average = first_4_total / 4
print(f"First 4 days average: {first_4_average}")


# Create total and average for last 4 days
last_4_total = sum(numbers[-4:])
last_4_average = last_4_total / 4
print(f"Last 4 days average: {last_4_average}")


# Create buy and sell signals based on crossing the 4-day moving average
for i in range(1, len(numbers) - 3):

    four_day_average = sum(numbers[i:i + 4]) / 4
    previous_four_day_average = sum(numbers[i - 1:i + 3]) / 4

    if (
        numbers[i + 3] > four_day_average
        and numbers[i + 2] <= previous_four_day_average
    ):
        signal.append("Buy")
        signal_days.append(i + 4)

    elif (
        numbers[i + 3] < four_day_average
        and numbers[i + 2] >= previous_four_day_average
    ):
        signal.append("Sell")
        signal_days.append(i + 4)


# Growth factor starts at 1, which represents 100% of starting principal
growth_factor = 1


# Calculate return from the beginning of the data to the first signal
# Assume the period before the first signal is opposite of the first signal
for i in range(len(signal_days)):

    first_signal_day = signal_days[i]

    if signal[i] == "Buy":

        starting_percent_change = (
            (numbers[0] - numbers[first_signal_day - 1])
            / numbers[0]
        ) * 100

        growth_factor *= (1 + starting_percent_change / 100)
        break

    elif signal[i] == "Sell":

        starting_percent_change = (
            (numbers[first_signal_day - 1] - numbers[0])
            / numbers[0]
        ) * 100

        growth_factor *= (1 + starting_percent_change / 100)
        break


# Compound returns from one signal to the next
for i in range(1, len(signal_days)):

    if signal[i - 1] == "Buy":

        new_percent_change = (
            (numbers[signal_days[i] - 1]
            - numbers[signal_days[i - 1] - 1])
            / numbers[signal_days[i - 1] - 1]
        ) * 100

        growth_factor *= (1 + new_percent_change / 100)

    elif signal[i - 1] == "Sell":

        new_percent_change = (
            (numbers[signal_days[i - 1] - 1]
            - numbers[signal_days[i] - 1])
            / numbers[signal_days[i - 1] - 1]
        ) * 100

        growth_factor *= (1 + new_percent_change / 100)


# Calculate the return from the final signal to the end of the data
last_signal_day = signal_days[-1]

if signal[-1] == "Buy":

    final_percent_change = (
        (numbers[-1] - numbers[last_signal_day - 1])
        / numbers[last_signal_day - 1]
    ) * 100

    growth_factor *= (1 + final_percent_change / 100)

elif signal[-1] == "Sell":

    final_percent_change = (
        (numbers[last_signal_day - 1] - numbers[-1])
        / numbers[last_signal_day - 1]
    ) * 100

    growth_factor *= (1 + final_percent_change / 100)


# Convert compounded growth back into a percentage
total_percent_change = (growth_factor - 1) * 100

print(
    f"Total compounded percent change from the start of the strategy "
    f"to the end of the strategy: {total_percent_change:.2f}%"
)





#Activity 2
#get user name and favorite color
user_name = input("What is your name? ")
usern_color = input("What is your favorite color? ")    
with open("user_info.txt", "w") as file:
    file.write(f"Name: {user_name}\n")
    file.write(f"Favorite Color: {usern_color}\n")


#Activity 3
#ask for user name 
user_name = input("What is your name? ")
#uppercase the name and print it
print(f"Welcome, {user_name.upper()}!")

#Activity 4
#store sentence
sentence = "dude, I just biked down that mountain and at first I was like " \
"Whoa, and then I was like Whoa"
#change first letter in sentence to uppercase
sentence = sentence[0].upper() + sentence[1:]
#change first instance of whoa to all lowercase
sentence = sentence.replace("Whoa", "whoa", 1)
#change second instance of whoa to all uppercase    
sentence = sentence.replace("Whoa", "WHOA", 1)
#add an exclamation point to the end of the sentence
sentence += "!"
#print the sentence
print(sentence)

#Activity 5
#list with three favorite colors
colors = ["blue", "green", "yellow"]
#use string join function to turn list into comma separated string
colors_string = ", ".join(colors)
beginning = "My favorite colors are: "
#combine beginning and colors_string into one string
combined_string = beginning + colors_string
#print the combined string
print(combined_string)

#Activity 6
#ask for user address
user_address = input("What is your address? ")
remove_spaces = user_address.replace(" ", "")
#use isalnum function to check if address is alphanumeric
if remove_spaces.isalnum():
    print("Your address is only letters and numbers. Congrats on being normal.")