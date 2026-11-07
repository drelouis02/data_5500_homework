import csv
#use csv.dictReader to read the csv file and store the data in a list of dictionaries
def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data
#convert the second column of the csv file to a list of floats
def convert_column_to_float(data, column_name):
    float_list = []
    for row in data:
        try:
            float_list.append(round(float(row[column_name]), 2))
        except ValueError:
            float_list.append(None)  # Handle non-convertible values
    return float_list
#store the result in a variable called prices
prices = convert_column_to_float(read_csv('AAPL.csv'), 'Close/Last')

print(prices[:5])

#create meanreversion trading strategy that buys when price is below 98% of 5 day average and sells when price is above 102% of average
#only for the fifth day and onwards, since we need 5 days of data to calculate the average
#add a 'Hold' signal for days where the price is within 2% of the 5-day average
def meanReversionStrategy(prices):
    holding = False
    total_profit = 0
    signals = []
    first_bought_price = None  # To track the price at which the first buy occurred
    for i in range(len(prices)):
        if i < 4:  # Not enough data to calculate 5-day average
            signals.append('Hold')
            continue
        
        five_day_avg = sum(prices[i-4:i+1]) / 5
        current_price = prices[i]
        
        if current_price < 0.98 * five_day_avg and not holding:
            signals.append('Buy')
            holding = True
            if first_bought_price is None:
                first_bought_price = current_price
            bought_price = current_price  # Update the bought price to the current price
            #print bought price rounded to 2 decimal places with $ sign
            print(f'Buying at: ${round(bought_price, 2)}')
        elif current_price > 1.02 * five_day_avg and holding:
            signals.append('Sell')
            total_profit += current_price - bought_price
            holding = False
            #print sell price rounded to 2 decimal places with $ sign
            print(f'Selling at: ${round(current_price, 2)}')
            #print profit rounded to 2 decimal places with $ sign
            print(f'trade profit: ${round(current_price - bought_price, 2)}')
        else:
            signals.append('Hold')
    #print rounded total profit to 2 decimal places with $ sign
    print(f'Total Profit: ${round(total_profit, 2)}')
    #calculate return profit percentage and print it rounded to 2 decimal places with % sign using the first bought price as the initial investment
    if first_bought_price is not None:
        return_percentage = (total_profit / first_bought_price) * 100
    else:
        return_percentage = 0
    print(f'Return Percentage: {round(return_percentage, 2)}%')
    #return the return profit percetage and the total profit both rounded to 2 decimal places
    return round(total_profit, 2), round(return_percentage, 2)

#create simple moving average trading strategy that buys when price is above simple moving average and sells when price is below simple moving average
def simpleMovingAverageStrategy(prices):
    holding = False
    total_profit = 0
    signals = []
    first_bought_price = None  # To track the price at which the first buy occurred
    for i in range(len(prices)):
        if i < 4:  # Not enough data to calculate 5-day average
            signals.append('Hold')
            continue
        
        five_day_avg = sum(prices[i-4:i+1]) / 5
        current_price = prices[i]
        
        if current_price > five_day_avg and not holding:
            signals.append('Buy')
            holding = True
            if first_bought_price is None:
                first_bought_price = current_price
            bought_price = current_price  # Update the bought price to the current price
            #print bought price rounded to 2 decimal places with $ sign
            print(f'Buying at: ${round(bought_price, 2)}')
        elif current_price < five_day_avg and holding:
            signals.append('Sell')
            total_profit += current_price - bought_price
            holding = False
            #print sell price rounded to 2 decimal places with $ sign
            print(f'Selling at: ${round(current_price, 2)}')
            #print profit rounded to 2 decimal places with $ sign
            print(f'trade profit: ${round(current_price - bought_price, 2)}')
        else:
            signals.append('Hold')
    #print rounded total profit to 2 decimal places with $ sign
    print(f'Total Profit: ${round(total_profit, 2)}')
    #calculate return profit percentage and print it rounded to 2 decimal places with % sign using the first bought price as the initial investment
    if first_bought_price is not None:
        return_percentage = (total_profit / first_bought_price) * 100
    else:
        return_percentage = 0
    print(f'Return Percentage: {round(return_percentage, 2)}%')
    #return the return profit percetage and the total profit both rounded to 2 decimal places
    return round(total_profit, 2), round(return_percentage, 2)


#create a list of tickers with the ten tickers
tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'META', 'TSLA', 'NVDA', 'FAST', 'CTAS', 'ADBE']
#create an empty dictionary to store the results of the strategies for each ticker
results = {}
#
for ticker in tickers:
    #read the csv file for the ticker
    prices = convert_column_to_float(read_csv(f'{ticker}.csv'), 'Close/Last')
    results[f"{ticker}_prices"] = prices
    #run the mean reversion strategy and store the results in the dictionary
    mr_profit, mr_returns = meanReversionStrategy(prices)
    #stores the result in results 
    results[f"{ticker}_mr_profit"] = mr_profit
    results[f"{ticker}_mr_returns"] = mr_returns
    #run the simple moving average strategy and store the results in the dictionary
    sma_profit, sma_returns = simpleMovingAverageStrategy(prices)
    results[f"{ticker}_sma_profit"] = sma_profit
    results[f"{ticker}_sma_returns"] = sma_returns

#function to save results to json file
def saveResults(results):
    import json
    with open('results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

saveResults(results)