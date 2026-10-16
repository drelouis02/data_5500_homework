#read in tsla txt file and st pric variable as float of numbers and 
#round it to two decimal places
file = open('TSLA.txt', 'r')
lines = file.readlines()
file.close()
#make price a list and strip the edges off
price = [float(line.strip()) for line in lines]
price = [round(p, 2) for p in price]
buy = []
sell = []
buy_day = []
sell_day = []
holding_stock = False
first_buy = 0
total_profit = 0
profit = 0

#loop through all the prices and calculate a five day moving average and create signals for buying and selling based on the moving average
for i in range(5, len(price)):
    five_day_prices = [price[j] for j in range(i - 5, i)]
    moving_average = sum(five_day_prices) / 5
    moving_average = round(moving_average, 2)
    #print(f"Five-day moving average starting from day {i+1}: {moving_average}")
    #print the price of i day 
    current_price = price[i]
    #print(f"The price of day {i+1} is {current_price}")
    #if statement to check if price is less than moving average * .98
    #if so update buy varaible with price and print message with day number
    if current_price < moving_average * 0.98:
        if holding_stock == False:
            buy.append(current_price)
            #add the buy day to the list of buy days
            buy_day.append(i + 1)
            holding_stock = True
            if first_buy == 0:
                first_buy = current_price
            #print message showing day of buy and price
            print(f"buying at:     {current_price}")
    #else if statement to check if price is greater than moving average * 1.02
    #update sell variable with price and print message with day number
    elif current_price > moving_average * 1.02:
        if holding_stock == True:
            sell.append(current_price)
            #add the sell day to the list of sell days
            sell_day.append(i + 1)

            #calculate profit from this trade
            profit = current_price - buy[-1]
            #add profit to total profit
            total_profit += profit
            holding_stock = False
        #print message showing day of sell and price
            print(f"selling at:    {current_price}")
            print(f"trade profit:  {profit:.2f}")
    else:
        pass

# Calculate final profit percentage
if first_buy != 0:
    final_profit_percentage = (total_profit / first_buy) * 100
else:
    final_profit_percentage = 0

# Print final results
print("--------------------")
print(f"Total profit:  {total_profit:.2f}")
print(f"first buy:     {first_buy}")
print(f"% return:      {final_profit_percentage:.2f}%") 
